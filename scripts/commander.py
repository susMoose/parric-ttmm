# python3

import subprocess
import queue
import threading
import statistics

global machines
global hostnames
global tasks
global level
global master_cube_N

hostnames = [
    'anchovy',
    'barracuda',
#    'blowfish',
#    'bonito',
#    'brill',
#    'char',
#    'cod',
#    'dorado',
#    'eel',
#    'flounder',
#    'grouper',
#    'halibut',
#    'herring',
#    'mackerel',
#    'marlin',
#    'perch',
#    'pollock',
#    'sardine',
#    'shark',
#    'sole',
#    'swordfish',
#    'tarpon',
#    'turbot',
#    'tuna',
#    'wahoo'
]


def partition(parent, segments):
    if not isinstance(parent, Cube):
        raise ValueError('passed non-Cube object as parent. parent must be a Cube')
    if segments < 1:
        raise ValueError('segments must be 1 or greater')

    children = []

    (x_p, y_p, z_p) = parent.c
    (x_p, y_p, z_p) = (x_p-parent.l//2, y_p-parent.l//2, z_p-parent.l//2) #convert center into point at bottom left
    step = int(parent.l / segments)  # if segments is 4 and parent.l is N, then step = N/4
    for x in range(0, segments): 
        x_c = x_p + x*step + step // 2
        for y in range(0, segments):
            y_c = y_p + y*step + step // 2
            for z in range(0, segments):
                z_c = z_p + z*step + step // 2
                child = Cube(center=(x_c,y_c,z_c), side_length=step)
                children.append(child)
    
    return children


class Cube:
    
    def __init__(self, center=None, side_length=2):
        (x, y, z) = center
        if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
            raise ValueError('origin must be integer tuple')
        if not isinstance(side_length, int):
            raise ValueError('side_length be an integer')
        self.c = center
        self.l = side_length

    def __str__(self):
        return str({'length': self.l, 'center': self.c})

    def center(self):
        return self.c


class Machine:
    def __init__(self, hostname):
        self.tasks = []
        self.hostname = hostname
        self.cores = self.calc_cores()
    
    def __str__(self):
        return str(self.hostname)

    def calc_cores(self):
        # $ lscpu | grep -i socket
        # Core(s) per socket:  8
        # Socket(s):           1
        cores_per_socket_pipe = subprocess.Popen(['echo', 'lscpu | grep -i "per socket"'] , stdout=subprocess.PIPE)
        cps_str = subprocess.Popen(['ssh', '-T', self.hostname], stdin=cores_per_socket_pipe.stdout, stdout=subprocess.PIPE).stdout.read()

        sockets_pipe = subprocess.Popen(['echo', 'lscpu | grep "Socket"'] , stdout=subprocess.PIPE)
        socks_str = subprocess.Popen(['ssh', '-T', self.hostname], stdin=sockets_pipe.stdout, stdout=subprocess.PIPE).stdout.read()

        cores_per_socket = int(cps_str.decode('utf-8').split(':')[1].replace(' ', ''))
        sockets = int(socks_str.decode('utf-8').split(':')[1].replace(' ', ''))

        return cores_per_socket * sockets


class Command:
    def __init__(self, executable, params):
        self.executable = executable
        self.params = params

    def __str__(self):
        p_str = ''
        for p in self.params:
            p_str += ' ' + str(p)
        return str(self.executable) + p_str

    def as_list(self):
        ret = [str(self.executable)]
        for p in self.params:
            ret.append(str(p))
        return ret
    
    def __hash__(self):
        return (self.executable, tuple(self.params)).__hash__()
    
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.executable==other.executable and self.params==other.params
    
    def __ne__(self, other):
        return not self==other

    def __lt__(self, other):
        #In case a tuple with a command at the end ties the previous results during a sort
        return self.__hash__() < other.__hash__()


class Result:
    def __init__(self, machine, core, command, time, level, parent):
        self.machine = machine
        self.core = core
        self.command = command
        self.time = time
        self.level = level
        self.parent = parent

    def __str__(self):
        ret = 'Result [' +  str(self.machine) + '-' + str(self.core) + '] : level-' + str(self.level)
        ret += ' : parent' + str(self.parent.c)
        ret += ' : ' + str(tuple(self.command.params[1:])) + ' : ' + str(self.time) + ' seconds'
        return ret

    def __lt__(self, other):
        return self.time < other.time

    def __gt__(self, other):
        return self.time > other.time


def init_machines():
    global machines
    global hostnames
    machines = []
    for h in hostnames:
        print('Creating','Machine(\''+str(h)+'\')...', end='')
        machines.append(Machine(h))
        print('done.')


def worker(machine, core, tasks, level, results, parent):
    #global tasks
    #global level
    while True:
        command = tasks.get()
        if not command:
            break

        # remotely invoke 'command' on 'machine' via ssh
        echo_pipe = subprocess.Popen(['echo', str(command)], stdout=subprocess.PIPE)
        ssh_pipe = subprocess.Popen(['ssh', '-T', str(machine.hostname)], stdin=echo_pipe.stdout, stdout=subprocess.PIPE)
        result_bytes = ssh_pipe.stdout.read()  # b'Execution time : 0.062362 sec.\n'
        #print('------>', result_bytes.decode('utf-8'))
        time = float(result_bytes.decode('utf-8').split(' ')[3])
        result = Result(machine, core, command, time, level, parent)
        if not command in results:
            results[command]=[]
        results[command].append(result)

        print(str(result))

        tasks.task_done()


def run_workers(machines, tasks, level, results, parent):
    #global results
    #global machines
    #global tasks

    threads = []
    for machine in machines:
        for i in range(0, machine.cores):
            t = threading.Thread(target=worker, args=(machine, i, tasks, level, results, parent))
            t.start()
            threads.append(t)
    tasks.join()

    for t in threads:
        tasks.put(None)

    for t in threads:
        t.join()

  
def main_helper(N=1000, partitions=[], path_prefix='./workspace/parric-ttmm/ttmm/alphaz_stuff/out', keep=[], iterations=3):
    global machines
    global master_cube_N
    master_cube_N = N
    init_machines()

    parent = Cube((N//2, N//2, N//2), N)
    tasks = queue.Queue()

    if not partitions:
        partitions = [2] * iterations
    if not keep:
        keep = [1] * iterations

    main_rec(0, parent, partitions, path_prefix, keep, iterations)


def main_rec(level, parent, partitions, path_prefix, keep, iterations):
    global master_cube_N
    
    if level >= iterations:
        return
    
    results={}
    # Add tasks to queue
    tasks = queue.Queue()
    print('\nCreating tasks for parent', parent.c,'...')
    for child in partition(parent, partitions[level]):
        (ts1, ts2, ts3) = child.center()
        for i in range(5):
            tasks.put(Command('{}/TMM'.format(path_prefix), [master_cube_N, ts1, ts2, ts3]))
    run_workers(machines, tasks, level, results, parent)
    print('...done.')
    
    # choose best results for next iteration, i.e. next set of parents
    sorted_results=[(results[command], command) for command in results]
    sorted_results=sorted([ ( statistics.mean([r.time for r in sr[0]]), sr[1]) for sr in sorted_results]) 
    print('\nChoosing best', keep[level], 'results...')
    for r in sorted_results[:keep[level]]:
        print('Selected :', tuple(r[1].params[1:]), str(r[0]), 'seconds')
        origin = tuple(r[1].params[1:]) # command.params = [1000, 250, 250, 750]
    print('...done.')

    for r in sorted_results[:keep[level]]: 
        main_rec(level+1, Cube(tuple(r[1].params[1:]), parent.l//partitions[level]), partitions, path_prefix, keep, iterations)



 

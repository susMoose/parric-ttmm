# python3

import subprocess
import queue
import threading

global machines
global hostnames
global tasks
global results
global level

hostnames = [
    'cod',
    'eel',
#    'flounder',
#    'dorado'
]


def partition(parent, segments):
    if not isinstance(parent, Cube):
        raise ValueError('passed non-Cube object as parent. parent must be a Cube')
    if segments < 1:
        raise ValueError('segments must be 1 or greater')

    children = []

    (x_p, y_p, z_p) = parent.o
    step = int(parent.l / segments)  # if segments is 4 and parent.l is N, then step = N/4
    for x in range(0, segments): 
        x_c = x_p + x*step
        for y in range(0, segments):
            y_c = y_p + y*step
            for z in range(0, segments):
                z_c = z_p + z*step
                child = Cube(origin=(x_c,y_c,z_c), side_length=step)
                children.append(child)
    
    return children


class Cube:
    
    def __init__(self, origin=(0,0,0), side_length=2):
        (x, y, z) = origin
        if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
            raise ValueError('origin must be integer tuple')
        if not isinstance(side_length, int):
            raise ValueError('side_length be an integer')
        self.o = origin
        self.l = side_length

    def __str__(self):
        return str({'length': self.l, 'origin': self.o, 'center': self.center()})

    def center(self):
        (x, y, z) = self.o 
        d = int(self.l / 2)
        return (x+d, y+d, z+d)


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
        cps_str = subprocess.Popen(['ssh', self.hostname], stdin=cores_per_socket_pipe.stdout, stdout=subprocess.PIPE).stdout.read()

        sockets_pipe = subprocess.Popen(['echo', 'lscpu | grep "Socket"'] , stdout=subprocess.PIPE)
        socks_str = subprocess.Popen(['ssh', self.hostname], stdin=sockets_pipe.stdout, stdout=subprocess.PIPE).stdout.read()

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


class Result:
    def __init__(self, machine, core, command, time, level):
        self.machine = machine
        self.core = core
        self.command = command
        self.time = time
        self.level = level

    def __str__(self):
        ret = '[' +  str(self.machine) + '-' + str(self.core) + '] : [level-' + str(self.level) + ']'
        ret += ' : ' + str(self.command) + ' : ' + str(self.time) + ' seconds'
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
        print('Creating','Machine(\''+str(h)+'\')...')
        machines.append(Machine(h))


def worker(machine, core):
    global tasks
    global results
    global level
    while True:
        command = tasks.get()
        if not command:
            break

        # remotely invoke 'command' on 'machine' via ssh
        echo_pipe = subprocess.Popen(['echo', str(command)], stdout=subprocess.PIPE)
        ssh_pipe = subprocess.Popen(['ssh', str(machine.hostname)], stdin=echo_pipe.stdout, stdout=subprocess.PIPE)
        result_bytes = ssh_pipe.stdout.read()  # b'Execution time : 0.062362 sec.\n'
        time = float(result_bytes.decode('utf-8').split(' ')[3])
        result = Result(machine, core, command, time, level)
        results.append(result)

        print(str(result))

        tasks.task_done()


def main(N=1000, partitions=[], path_prefix='./workspace/parric-ttmm/ttmm/alphaz_stuff/out', keep=[]):
    global tasks
    global results
    global level

    if not keep:
        keep = [1] * 100

    if not partitions:
        partitions = [2] * 100

    init_machines()
    
    # FIRST level - add tasks to queue
    level = 0
    parent = Cube((0,0,0), N)
    tasks = queue.Queue()
    for child in partition(parent, partitions[0]):
        (ts1, ts2, ts3) = child.center()
        tasks.put(Command('{}/TMM'.format(path_prefix), [N, ts1, ts2, ts3]))

    threads = []
    results = []
    for machine in machines:
        for i in range(0, machine.cores):
            #print('--> setup', machine, i)
            t = threading.Thread(target=worker, args=(machine, i))
            t.start()
            threads.append(t)
    tasks.join()

    for machine in machines:
        for i in range(0, machine.cores):
            tasks.put(None)
    for t in threads:
        t.join()


    # SECOND level
    level = 1
    parents = []
    tasks = queue.Queue()
    results.sort()
    N1 = int(N / partitions[0])
    for r in results[:keep[0]]:
        print('Selected :', tuple(r.command.params[1:]))
        origin = tuple(r.command.params[1:]) # command.params = [1000, 250, 250, 750]
        parents.append(Cube(origin, N1))
    
    for parent in parents:
        for child in partition(parent, partitions[1]):
            (ts1, ts2, ts3) = child.center()
            tasks.put(Command('{}/TMM'.format(path_prefix), [N, ts1, ts2, ts3]))    

    for t in list(tasks.queue):
        print('New task :', str(t)) 

    return results, tasks
        
        
        
        



















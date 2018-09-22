import os
import subprocess
import matplotlib.pyplot as plt

def map(N=1000, step=100, path_prefix=None, toFile=False):

    if not path_prefix:
        path_prefix = './ttmm/alphaz_stuff/out'

    points = {}

    for ts1 in range(step, N+step, step):
        for ts2 in range(step, N+step, step):
            for ts3 in range(step, N+step, step):
                executable = '{}/TMM'.format(path_prefix)
                if toFile:
                    out_file = '/tmp/results/TMM_{}_{}_{}_{}'.format(N, ts1, ts2, ts3)
                    command_str = '{} {} {} {} {} > {}'.format(executable, N, ts1, ts2, ts3, out_file)
                    tmm_pipe = subprocess.Popen(command_str, shell=True)
                    tmm_pipe.wait()
                    print(command_str)
                else:
                    command = [executable, str(N), str(ts1), str(ts2), str(ts3)]
                    tmm_pipe = subprocess.Popen(command, stdout=subprocess.PIPE)
                    (raw_bytes, _) = tmm_pipe.communicate()
                    tmm_pipe.wait()
                    time = raw_bytes.decode('utf-8').split(' ')[3] # raw_bytes = b'Execution time : 0.042333 sec.\n'
                    points[(ts1, ts2, ts3)] = time
                    print(executable, N, ts1, ts2, ts3, ' --> ', time)

    return points if points else None


def load_points(dir='results'):
    results = {}
    for file_name in os.listdir(dir):
        file = open('{}/{}'.format(dir, file_name), 'r')
        line = file.readline()
        time = line.split(' ')[3]
        file.close()
        
        atts = file_name.split('_')
        N = atts[1]
        ts1, ts2, ts3 = atts[2], atts[3], atts[4]

        results[(ts1, ts2, ts3)] = time
    
    return results


def graph(points):
    # some python snippets here: https://towardsdatascience.com/the-art-of-effective-visualization-of-multi-dimensional-data-6c7202990c57
    fig = plt.figure(figsize=(8, 6))
    t = fig.suptitle('TMM (N=5000) ts1 - ts2 - ts3', fontsize=14)
    ax = fig.add_subplot(111, projection='3d')

    data_points = [point for point in points]
    colors = ['red' for point in points]

    for data, color in zip(data_points, colors):
        x, y, z = data
        ax.scatter(x, y, z, alpha=0.4, c=color, edgecolors='none', s=30)

    ax.set_xlabel('ts1')
    ax.set_ylabel('ts2')
    ax.set_zlabel('ts3')

    fig.savefig('foo.pdf', bbox_inchecs='tight')


    




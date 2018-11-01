import subprocess
import numpy as np
from statistics import mean


def compile():
    tile_sizes = np.arange(start=1000, stop=5000, step=1000)
    for ts1 in tile_sizes:
        for ts2 in tile_sizes:
            for ts3 in tile_sizes:
                # compile one with hardcoded sizes
                cmd = 'make -fMakefileHARD SIZE1={} SIZE2={} SIZE3={}'.format(ts1, ts2, ts3)
                subprocess.Popen(cmd.split(' '))



def main(N=5000):
    tile_sizes = np.arange(start=1000, stop=N, step=1000)
    for ts1 in tile_sizes:
        for ts2 in tile_sizes:
            for ts3 in tile_sizes:
                cmd = './TMM {} {} {} {}'.format(N, ts1, ts2, ts3)
                cmdH = './TMMH_{}_{}_{} {} 1 1 1'.format(ts1, ts2, ts3, N)
                cmdH_pretty = './TMMH_{}_{}_{} {}'.format(ts1, ts2, ts3, N)
               
                # with parameters passed at runtime
                cmd_times = [] 
                print('{} '.format(cmd), end='')
                for trial in range(3):
                    p = subprocess.Popen(cmd.split(' '), stdout=subprocess.PIPE)
                    t = float(p.stdout.read().decode('utf-8').split(' ')[3])
                    p.wait()
                    cmd_times.append(t)
                mean_tmm = mean(cmd_times)
                print(' --> {:.5f} sec'.format(mean_tmm))

                # hardcoded parameters
                cmd_times = []
                print('{} '.format(cmdH_pretty), end='')
                for trial in range(3):
                    p = subprocess.Popen(cmdH.split(' '), stdout=subprocess.PIPE)
                    t = float(p.stdout.read().decode('utf-8').split(' ')[3])
                    p.wait()
                    cmd_times.append(t)
                mean_tmmh = mean(cmd_times)
                print('--> {:.5f} sec  => RATIO : {}'.format(mean_tmmh, mean_tmmh / mean_tmm))
                print()

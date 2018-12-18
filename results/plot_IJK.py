import sys
import os
import argparse
import numpy as np
import matplotlib.pyplot as plt


class Result:
    def __init__(self, N, t1, t2, t3, time):
        self.N = N
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.gflops = N*N*N*(1.0/3.0)*(10**-9)
        self.time = time

    def __str__(self):
        return 'N={}, TS=({},{},{}), time={}'.format(self.N, self.t1, self.t2, self.t3, self.time)

    def __hash__(self):
        return hash('{}-{}-{}-{}'.format(self.N, self.t1, self.t2, self.t3))

    def __eq__(self, other):
        if (self.N != other.N) or (self.t1 != other.t1) or (self.t2 != other.t2) or (self.t3 != other.t3):
            return False
        else:
            return True


def load_results(args):
    results = []
    # parse raw results from file
    file_name = args['file_path']
    f=open(file_name,"r")
    for line in f:
        if not line.startswith('Result'):
            continue
        line = line.replace(' ','')
        pcs = line.split(':')
        N = int(pcs[1].split('=')[1])
        TS = pcs[2].replace('(','').replace(')','').split(',')
        ts1, ts2, ts3 = int(TS[0]), int(TS[1]), int(TS[2])
        time = float(pcs[3].split('s')[0])
        results.append(Result(N, ts1, ts2, ts3, time))
    return results


def avg_results(all_results):
    results = {}
    for r in all_results:
        if r not in results:
            results[r] = [r.time]
        else:
            results[r].append(r.time) 

    avgs = {}
    for r in results:
        times = np.sort(results[r])
        avg = np.mean(times[1:-1])
        avgs[r] = avg
    return avgs


def main(all_results):
    results = avg_results(all_results)
    points = {}
    for r in results:
        time = results[r]
        if r.N not in points:
            points[r.N] = {'TS':[r.t1], 'gfps':[r.gflops/time], 'times':[r.time]}
        else:
            points[r.N]['TS'].append(r.t1)
            points[r.N]['times'].append(r.time)
            points[r.N]['gfps'].append(r.gflops/time)

    for N in points:
        print(N, 'typ', type(N))
        print('\t', points[N]['TS'])
        print('\t', points[N]['times'])
        print('\t', points[N]['gfps']) 

    plt.scatter(points[5000]['TS'], points[5000]['gfps'])








if __name__ == '__main__':
    program_name = os.path.basename(sys.argv[0])
    # parse command line arguments
    parser = argparse.ArgumentParser(prog=program_name)
    parser.add_argument('-f', '--file-path', help='results file path', default='')
    args = vars(parser.parse_args())
    results = load_results(args)
    sys.exit(main(results))


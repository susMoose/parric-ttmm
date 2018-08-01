

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


''' If print(cube, cube.center()) = {'length': 1666, 'origin': (0, 0, 0)} (833, 833, 833)
    Then this returns:
        ./TMM 
'''
def make_command(N, cube, path_prefix='.'):
    executable = '{}/TMM'.format(path_prefix)
    (ts1, ts2, ts3) = cube.center()
    command = [executable, str(N), str(ts1), str(ts2), str(ts3)]
    return command


def main(N=1000, partitions=2):
    parent = Cube((0,0,0), N)
    
    for child in partition(parent, partitions):
        print(child)
    








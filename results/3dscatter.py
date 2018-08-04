if __name__ == "__main__":
    import matplotlib.pyplot as plot
    from mpl_toolkits.mplot3d import Axes3D
    size=5000
    points=[]
    f=open("experiment-20180804.opt","r")
    for line in f:
        line=line.split(" ")
        print(line)
        point=( float(line[2][1:-1]), float(line[3][:-1]), float(line[4][:-1]))
        point=(point[0], point[1], point[2])
        points.append(point)
    
    fig=plot.figure()
    graph=fig.add_subplot(111, projection="3d")
    graph.scatter([p[0] for p in points], [p[1] for p in points], [p[2] for p in points] )
    graph.set_xlabel("ts1")
    graph.set_ylabel("ts2")
    graph.set_zlabel("ts3")
    graph.set_xlim3d(0,1000)
    graph.set_ylim3d(0,1000)
    graph.set_zlim3d(0,1000)
plot.show()

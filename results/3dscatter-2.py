if __name__ == "__main__":
    import matplotlib.pyplot as plot
    from mpl_toolkits.mplot3d import Axes3D
    size=5000
    points=[]
    f=open("experiment-20180805.log","r")
    for line in f:
        line=line.split(" ")
        if line[0] != "Result":
            continue
        #print(line)
        point=( float(line[10][:-1]), float(line[11][:-1]))
        time = float(line[-2])
        gflops= (41 + (2/3) ) / time
        point=(point[0], point[1], gflops)
        points.append((gflops, point))
    f.close()
    #points.sort()
    #series_boundary=0
    #for i in range(len(points)):
    #    if points[i][0] > 12:
    #        series_boundary=i
    #        break
    
    
    points=[p[1] for p in points]
    fig=plot.figure()
    graph=fig.add_subplot(111, projection="3d")
    graph.scatter([p[0] for p in points], [p[1] for p in points], [p[2] for p in points])
    
    #graph.scatter([p[0] for p in points[series_boundary:]], [p[1] for p in points[series_boundary:]], [p[2] for p in points[series_boundary:]], label=">12" )
    
    graph.set_xlabel("ts2")
    graph.set_ylabel("ts3")
    graph.set_zlabel("gflops")
    graph.set_xlim3d(0,5000)
    graph.set_ylim3d(0,5000)
    graph.set_zlim3d(0,13)
    #graph.legend()
    plot.show()

if __name__ == "__main__":
    import matplotlib.pyplot as plot
    from mpl_toolkits.mplot3d import Axes3D
    size=5000
    points=[]
    fs = ["experiment-20180804.opt","experiment-20180805.opt"]
    for name in fs:
        f=open(name,"r")
        for line in f:
            line=line.split(" ")
            print(line)
            point=( float(line[2][1:-1]), float(line[3][:-1]), float(line[4][:-1]))
            gflops = float(line[-2])
            points.append((gflops, point))
   
        
    
    points.sort()
    series_boundary=0
    for i in range(len(points)):
        if points[i][0] > 12:
            series_boundary=i
            break
    
    
    points=[p[1] for p in points]
    fig=plot.figure()
    graph=fig.add_subplot(111, projection="3d")
    graph.scatter([p[0] for p in points[:series_boundary]], [p[1] for p in points[:series_boundary]], [p[2] for p in points[:series_boundary]], label="<12" )
    
    graph.scatter([p[0] for p in points[series_boundary:]], [p[1] for p in points[series_boundary:]], [p[2] for p in points[series_boundary:]], label=">12" )
    
    graph.set_xlabel("ts1")
    graph.set_ylabel("ts2")
    graph.set_zlabel("ts3")
    graph.set_xlim3d(0,5000)
    graph.set_ylim3d(0,5000)
    graph.set_zlim3d(0,5000)
    graph.legend()
    plot.show()

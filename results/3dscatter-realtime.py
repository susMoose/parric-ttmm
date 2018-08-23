if __name__ == "__main__":
    import matplotlib.pyplot as plot
    import matplotlib.cm as cm
    from mpl_toolkits.mplot3d import Axes3D
    size=5000

    points=[]
    all_points={}
    cnt = 0
    fs = ["experiment-20180805.log"]
    for name in fs:
        f=open(name,"r")
        for line in f:
            line=line.split(" ")
            if line[0] != "Result":
                continue
            cnt += 1
            p=( float(line[9][1:-1]), float(line[10][:-1]), float(line[11][:-1]))
            time = float(line[-2])
            gflops= (41 + (2/3) ) / time
            point=(p[0], p[1], p[2], gflops)
            if p in all_points:
                all_points[p].append(gflops)
            else:
                all_points[p] = [gflops]
        f.close()
    
    for p in all_points:
        l = all_points[p]
        avg_gflops = sum(l) / len(l)
        point = (p[0], p[1], p[2], avg_gflops)
        points.append((avg_gflops, point))
    
    print(cnt, len(points))
    points.sort()
    
    points=[p[1] for p in points]
    sb = 0
    for i in range(len(points)):
        if points[i][3] > 11.75:
            sb = i
            break;
    
    fig=plot.figure()
    graph=fig.add_subplot(111, projection="3d")
    
    
    
    s = graph.scatter([p[0] for p in points], [p[1] for p in points], [p[2] for p in points], c=[p[3] for p in points], cmap=cm.YlOrRd)
    graph.set_xlabel("ts1")
    graph.set_ylabel("ts2")
    graph.set_zlabel("ts3")
    graph.set_xlim3d(0,5000)
    graph.set_ylim3d(0,5000)
    graph.set_zlim3d(0,5000)
    
    

    plot.show()



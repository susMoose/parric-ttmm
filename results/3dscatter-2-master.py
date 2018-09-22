if __name__ == "__main__":
    import matplotlib.pyplot as plot
    import matplotlib.cm as cm
    from mpl_toolkits.mplot3d import Axes3D
    size=5000

    points=[]
    all_points={}
    cnt = 0
    fs = ["experiment-20180805.log"]#, "experiment-20180804.log"]
    for name in fs:
        f=open(name,"r")
        for line in f:
            line=line.split(" ")
            if line[0] != "Result":
                continue
            cnt += 1
            #print(line)
            # point=( float(line[2][1:-1]), float(line[3][:-1]), float(line[4][:-1]))
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
        #print('all_points[{}]'.format(p), all_points[p],'  --->  ', '({},{},{})'.format(p[0],p[1],p[2],avg_gflops))
        #avg_gflops = 0
        #for pair in point:
        #    (gflops, _) = pair
        #    avg_gflops += gflops
        #avg_gflops /= len(point)
        #points.append((avg_gflops,point[1]))
    
    print(cnt, len(points))
    points.sort()

    #print('--MAX--->',points[-1])

    #series_boundary=0
    #for i in range(len(points)):
    #    if points[i][0] > 12:
    #        series_boundary=i
    #        break
    
    points=[p[1] for p in points]
    sb = 0
    for i in range(len(points)):
        if points[i][3] > 11.75:
            sb = i
            break;
    #print('$$$>', sb, len(points))
    
    fig=plot.figure()
    t1x2xFL_graph=fig.add_subplot(111, projection="3d")
    # ts1-2
#    t1x2xFL_graph.scatter([p[0] for p in points[:sb]], [p[1] for p in points[:sb]], [p[3] for p in points[:sb]])
#    t1x2xFL_graph.scatter([p[0] for p in points[sb:]], [p[1] for p in points[sb:]], [p[3] for p in points[sb:]], c=[p[3] for p in points[sb:]], cmap=cm.plasma)
    t1x2xFL_graph.scatter([p[0] for p in points], [p[1] for p in points], [p[2] for p in points], c=[p[3] for p in points], cmap=cm.YlOrRd)
    t1x2xFL_graph.set_xlabel("ts1")
    t1x2xFL_graph.set_ylabel("ts2")
    t1x2xFL_graph.set_zlabel("ts3")
    t1x2xFL_graph.set_xlim3d(0,5000)
    t1x2xFL_graph.set_ylim3d(0,5000)
    t1x2xFL_graph.set_zlim3d(0,5000)
#    
#    # ts1-3
#    t1x3xFL_graph=fig.add_subplot(111, projection="3d")
#    t1x3xFL_graph.scatter([p[0] for p in points], [p[2] for p in points], [p[3] for p in points], c=[p[3] for p in points], cmap=cm.YlOrRd)
    #t1x3xFL_graph.set_xlabel("ts1")
    #t1x3xFL_graph.set_ylabel("ts3")
#    t1x3xFL_graph.set_zlabel("GigaFlops / sec")
#    t1x3xFL_graph.set_xlim3d(0,5000)
#    t1x3xFL_graph.set_ylim3d(0,5000)
#    t1x3xFL_graph.set_zlim3d(0,13)
#    
#    # ts2-3
#    t2x3xFL_graph=fig.add_subplot(111, projection="3d")
#    t2x3xFL_graph.scatter([p[0] for p in points], [p[1] for p in points], [p[2] for p in points], c=[p[3] for p in points], cmap=cm.YlOrRd)
#    t2x3xFL_graph.set_xlabel("ts1")
#    t2x3xFL_graph.set_ylabel("ts2")
#    t2x3xFL_graph.set_zlabel("ts3")
#    t2x3xFL_graph.set_xlim3d(0,5000)
#    t2x3xFL_graph.set_ylim3d(0,5000)
#    t2x3xFL_graph.set_zlim3d(0,5000)




    points = points[sb:]
    import numpy as np

    # smallers
#    t1x2xFL_graph=fig.add_subplot(111, projection="3d")
#    # ts1-2
#    t1x2xFL_graph.scatter([p[0] for p in points], [p[1] for p in points], [p[3] for p in points], c=[p[3] for p in points], cmap=cm.PuRd)
#    #t1x2xFL_graph.set_xlabel("ts1")
#    #t1x2xFL_graph.set_ylabel("ts2")
#    t1x2xFL_graph.set_zlabel("GigaFlops / sec")
#    #major_ticks = np.arange(19, 21.05, .5)
#    #minor_ticks = np.arange(0, 1400, 400)
#    #t1x2xFL_graph.set_xticks(major_ticks)
#    #t1x2xFL_graph.set_xticks(minor_ticks, minor=True)

    
#    # ts1-3
#    t1x3xFL_graph=fig.add_subplot(111, projection="3d")
#    t1x3xFL_graph.scatter([p[0] for p in points], [p[2] for p in points], [p[3] for p in points], c=[p[3] for p in points], cmap=cm.PuRd)
    #t1x3xFL_graph.set_xlabel("ts1")
    #t1x3xFL_graph.set_ylabel("ts3")
#    t1x3xFL_graph.set_zlabel("GigaFlops / sec")
#    
    # ts2-3
#    t2x3xFL_graph=fig.add_subplot(111, projection="3d")
#    t2x3xFL_graph.scatter([p[1] for p in points], [p[2] for p in points], [p[3] for p in points], c=[p[3] for p in points], cmap=cm.PuRd)
    #t2x3xFL_graph.set_xlabel("ts2")
    #t2x3xFL_graph.set_ylabel("ts3")
#    t2x3xFL_graph.set_zlabel("GigaFlops / sec")











    plot.show()







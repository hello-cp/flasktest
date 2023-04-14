import networkx as nx
coordinate = []

def Dijstrle():
    G = nx.Graph(my_g='my_graph')  # 无向图
    final_poi = ['栾川重渡沟风景区', '王城公园', '龙门石窟', '洛阳老街', '白马寺']
    nodes = []
    for k in final_poi:
        nodes.append(all_poi[k].name)
        coordinate.append(all_poi[k].location)

    t = len(nodes)
    distance = []
    for i in range(0, t - 1):
        for j in range(i + 1, t):
            tt1 = str(cooedinate[i][0])
            mm1 = str(cooedinate[i][1])
            road1 = tt1 + ',' + mm1
            lon2, lat2 = coordinate[j]
            d = get_distance_hav(lon1, lat1, lon2, lat2)
            a = [nodes[i], nodes[j], {'weight': d}]
            b = tuple(a)
            distance.append(b)
    G.add_nodes_from(nodes)
    G.add_edges_from(distance)

    final = copy.deepcopy(nodes)
    d = [0] * 20
    a = [0] * 20
    dmin = 99999
    print("最短路线：")
    for j in nodes:
        start = j
        l = copy.deepcopy(nodes)
        l.remove(start)
        t = len(l)

        for i in range(0, t - 1):
            end = l[i]
            temp = copy.deepcopy(l)
            print(end)
            temp.remove(end)
            a[i] = min([path  # 返回 key 为最小值的 path
                        for path in nx.all_simple_paths(G, source=start, target=end)  # gAnt 中所有起点为A、终点为E的简单路径
                        if all(n in path for n in temp)],  # 满足路径中包括顶点 B,C,D
                       key=lambda x: sum(G.edges[edge]['weight'] for edge in nx.utils.pairwise(x)))  # key 为加权路径长度

            d[i] = sum(G.edges[edge]['weight'] for edge in nx.utils.pairwise(a[i]))
            print(a[i])
            print(d[i])
            if (d[i] < dmin) & (i >= 0):
                dmin = d[i]
                print("最小值", dmin)
                final = a[i]
    print(final)
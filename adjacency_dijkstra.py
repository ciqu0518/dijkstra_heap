#链式前向星+dijkstra
def dijkstra(graph,head,src): 
    nodes = [key for key in head]    #取出所有节点
    distance = {}    #起点到所有顶点的距离，初始为无穷大，起点到起点为零
    for i in nodes:
        distance[i] = float('inf')         #一开始到所有节点的距离都为无穷大
    distance[src] = 0
    visited = []    #已经确定了最短路径的节点
    v = src       #每次迭代中选出的最短路径对应的节点
    
    while len(visited)<len(nodes):    #已经确定最短路径的节点数小于总的节点数
        visited.append(v)
        pos = head[v]    #以V为起点的边里面第一条边的位置
        while pos > -1:
            to = graph[pos]['to']
            weight = graph[pos]['weight']
            new_dist = distance[v] + weight    
            if new_dist < distance[to]:
                distance[to] = new_dist    #如果与V直接相连的边能缩短对应顶点的到源顶点的距离，则替代distancez中的值
            pos = graph[pos]['next']
        
        dist = distance.copy()
        for i in  visited:
            del dist[i]
        if len(dist) != 0:
            v = min(dist,key=dist.get)   #找到distance中除去VISITED中的点以后的最小值对应的顶点，作为下一个V
    return distance
                

def add_edge(src,dest,weight):
    node = src
    a = node in head
    if a == False:
        head[node] = -1    #节点I第一次出现，将以节点I起点的第一条边的存储位置初始化为-1
  
    edge_dict = {}
    edge_dict['to'] = dest
    edge_dict['next'] = head[node]
    edge_dict['weight'] = weight
    edge_list.append(edge_dict)
    head[node] = len(edge_list) - 1
    
if __name__ == '__main__':
    graph_list = [
            [0, 2, 1, 4, 5, 1],
            [1, 0, 4, 2, 3, 4],
            [2, 1, 0, 1, 2, 4],
            [3, 5, 2, 0, 3, 3],
            [2, 4, 3, 4, 0, 1],
            [3, 4, 7, 3, 1, 0]]
     #将邻接矩阵转换成 [src,dest,weight] 的数组
    input_edge = []   
    for i in range(len(graph_list)):
        for j in range(len(graph_list)):
            if i != j:
                edge = [i,j,graph_list[i][j]]
                input_edge.append(edge)
    
    edge_list = []   #list,存储边
    head = {}   #字典，表示以I为起点的第一条边存储的位置

    for edge in input_edge:
        add_edge(edge[0],edge[1],edge[2])
   
    dist = dijkstra(edge_list,head,5)
    print(dist)
    

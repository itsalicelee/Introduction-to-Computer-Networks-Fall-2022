import os 
import sys

MAX_DISTANCE = 1e8
# P1 script: python hw2.py p1_test1.txt
# P2 script: python hw2.py p1_test1.txt [Removed Router Number]
class Graph():
    def __init__(self, vertices_num, graph):
        self.v = vertices_num
        self.graph = graph
                
    def dijkstra(self, src):
        # initialize 
        dist = [MAX_DISTANCE] * self.v
        unvisited = [True] * self.v
        hop = [-1] * self.v
        
        unvisited[src] = False
        dist[src] = 0
        hop[src] = src
        min_node = src
        
        for i in range(self.v):
            min_dist = MAX_DISTANCE
            # find the min_dist and min_node
            for v in range(self.v):
                if dist[v] < min_dist and dist[v] != -1 and unvisited[v] == True:
                    min_dist = dist[v]
                    min_node = v
            unvisited[min_node] = False
            # print("min_node", min_node)            
            # relax vertex v using min_node
            for v in range(self.v):
                if( self.graph[min_node][v] > 0 and unvisited[v] == True and 
                   dist[v] > dist[min_node] + self.graph[min_node][v]):
                    dist[v] = dist[min_node] + self.graph[min_node][v]            
                    if min_node == src:
                        hop[v] = v
                    else:
                        hop[v] = hop[min_node]
            # print("dist", dist)
            # print("hop", hop)
        return dist, hop

def writeFile(filename, dists, hops, to_remove):
    cnt = 1
    with open(filename, 'w') as f:
        for i in range(len(dists)):
            if cnt == to_remove:
                cnt += 1
                continue
            f.write('Routing table of router {}:\n'.format(cnt))
            for j in range(len(hops)):
                if(hops[i][j] == -1):
                    f.write('-1 -1\n')
                else:    
                    f.write(str(dists[i][j]) + ' ' + str(hops[i][j]+1) + '\n')
            cnt += 1

def readFile(filename):
    with open(os.path.join('./testcase', filename), 'r') as f:
        lines = f.readlines()
        num = int(lines[0])
        graph_str = [i.strip().split(' ') for i in lines[1:]]
        graph = []
        for i in graph_str:
            graph.append([int(j) for j in i])
        # print(num, graph)
    return num, graph


if __name__ == '__main__':
    if len(sys.argv) == 2: # problem 1 
        filename = sys.argv[1]
        to_remove = 0 # nothing to remove!
        output_filename = os.path.join('./testcase', filename[:-4]+'_GenTable.txt')
        num, graph = readFile(filename)
        
    elif len(sys.argv) == 3: # problem 2
        filename = sys.argv[1]
        to_remove = int(sys.argv[2])
        output_filename = os.path.join('./testcase', filename[:-4]+'_RmRouter'+str(to_remove)+ '.txt')
        num, graph = readFile(filename)
        for i in range(num):
            graph[i][to_remove-1] = -1
    # print(graph)
    g  = Graph(vertices_num=num, graph=graph)
    
    dists = []
    hops = []
    for i in range(num):
        dist, hop = g.dijkstra(i)
        dists.append(dist)
        hops.append(hop)
    # print(dists, hops)
    writeFile(output_filename, dists, hops, to_remove)
    
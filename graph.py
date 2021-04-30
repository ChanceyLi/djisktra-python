# This is a sample Python script.
import sys


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Graph():
    # 用于拓扑图路径规划，对于graph[i][j] = k,表示点i,j之间的代价是k
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printSolution(self, dist, list):
        print("Vertex \tDistance from Source \tlist")
        for node in range(self.V):
            print(node, "\t", dist[node], "\t\t\t", list[node])

    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        min_index = 0
        for v in range(self.V):
            if dist[v] < min and not sptSet[v]:
                min = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        lst = [0] * self.V
        sptSet = [False] * self.V

        for count in range(self.V):
            u = self.minDistance(dist, sptSet)

            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not sptSet[v] and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    lst[v] = u
        return dist, lst


class GraphMatrix(Graph):
    # 用于机器人二维图路径规划，graph[i][j] = k，表示从相邻点到达[i,j]点的代价是k
    def __init__(self, vertices):
        super().__init__(vertices)

    def printSolution(self, dist, lst, point, str):
        ret = [[0 for column in range(self.V)] for row in range(self.V)]
        ret[str[0]][str[1]] = 1
        x, y = point[0], point[1]
        while [x, y] != str:
            ret[x][y] = 1
            x, y = lst[x][y]
        for u in range(self.V):
            for v in range(self.V):
                print(ret[u][v], end="\t")
            print()

    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        min_index = [0, 0]
        for u in range(self.V):
            for v in range(self.V):
                if dist[u][v] < min and not sptSet[u][v]:
                    min = dist[u][v]
                    min_index = [u, v]
        return min_index

    def dijkstra(self, src):
        dist = [[sys.maxsize for column in range(self.V)] for row in range(self.V)]
        dist[src[0]][src[1]] = 0
        lst = [[[0, 0] for column in range(self.V)] for row in range(self.V)]
        sptSet = [[False for column in range(self.V)] for row in range(self.V)]
        for c in range(self.V):
            for s in range(self.V):
                u, v = self.minDistance(dist, sptSet)
                sptSet[u][v] = True
                for m, n in [[u - 1, v], [u, v - 1], [u + 1, v], [u, v + 1]]:
                    if 0 <= m < self.V and 0 <= n < self.V and not sptSet[m][n] and dist[m][n] > dist[u][v] + \
                            self.graph[m][n]:
                        dist[m][n] = dist[u][v] + self.graph[m][n]
                        lst[m][n] = [u, v]

        return dist, lst

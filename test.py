import graph
# 测试GraphMatrix中的二维图方法
g = graph.GraphMatrix(9)
g.graph = [[0, 4, 4, 4, 4, 4, 4, 4, 4],
        [0, 4, 4, 4, 4, 4, 4, 4, 4],
        [0, 0, 4, 4, 4, 4, 4, 4, 4],
        [4, 0, 0, 0, 4, 4, 4, 4, 4],
        [4, 4, 4, 0, 0, 4, 4, 4, 4],
        [4, 4, 4, 4, 0, 0, 4, 4, 4],
        [4, 4, 4, 4, 4, 0, 0, 4, 4],
        [4, 4, 4, 4, 4, 4, 0, 0, 0],
        [4, 4, 4, 4, 4, 4, 4, 4, 0]
        ]
dist, lst = g.dijkstra([0,0])
g.printSolution(dist, lst,[8,8],[0,0])

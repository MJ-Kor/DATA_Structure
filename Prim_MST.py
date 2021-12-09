INF = 9999
def getMinVertex(dist, selected):
    minv = 0
    mindist = INF
    for v in range(len(dist)):
        if not selected[v] and dist[v]<mindist:
            mindist = dist[v]
            minv = v
    return minv

def Prim_MST(vertex, adj):
    vsize = len(vertex)
    dist = [INF] * vsize
    selected = [False] * vsize                                         # selected는 무방향 그래프이므로 중복을 방지하려고 만든것
    dist[0] = 0

    for i in range(vsize):                                              # 최단 거리로 이동한 정점에 대해서 경로들을 dist에 저장하는 루트
        u = getMinVertex(dist, selected)
        selected[u] = True
        print(vertex[u], end =' ')
        for v in range(vsize):
            if (adj[u][v] != None):
                if selected[v] == False and adj[u][v] < dist[v]:        # 현재 정점으로부터 다른 정점들로까지의 거리를 dist에 저장
                    dist[v] = adj[u][v]
    print()

vertex = ['A','B','C','D','E','F','G']
adjMat = [[None, 29  , None, None, None, 10  , None],
          [29  , None, 16  , None, None, None, 15  ],
          [None, 16  , None, 12  , None, None, None],
          [None, None, 12  , None, 22  , None, 18  ],
          [None, None, None, 22  , None, 27  , 25  ],
          [10  , None, None, None, 27  , None, None],
          [None, 15  , None, 18  , 25  , None, None]]

Prim_MST(vertex, adjMat)

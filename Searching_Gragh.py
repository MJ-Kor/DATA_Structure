import collections as cols


mygraph = {'A':{'B','C'},
           'B':{'A','D'},
           'C':{'A','D','E'},
           'D':{'B','C','F'},
           'E':{'C','G','H'},
           'F':{'D'},
           'G':{'E','H'},
           'H':{'E','G'}
           }

def DFS(graph, start, visited = set()):
    if start not in visited:
        visited.add(start)
        print(start, end='')
        nbr = graph[start] - visited        # 집합 자료형의 차집합 '-'
        for v in nbr:
            DFS(graph, v, visited)

def BFS(graph, start):
    visited = set([start])
    queue = cols.deque([start])
    while queue:                            # 공백이 아닐 때 까지
        vertex = queue.popleft()
        print(vertex, end = '')
        nbr = graph[vertex] - visited
        for v in nbr:
            visited.add(v)
            queue.append(v)


def DFS_cc(graph, color, vertex, visited):
    if vertex not in visited:
        visited.add(vertex)
        color.append(vertex)
        nbr = graph[vertex] - visited
        for v in nbr:
            DFS_cc(graph, color, v, visited)
    return color

def find_connected_component(graph):
    visited = set()
    colorList = []

    for vtx in graph:
        if vtx not in visited:
            color = DFS_cc(graph, [], vtx, visited)
            colorList.append(color)

    print("그래프 연결성분 개수 = %d" %len(colorList))
    print(colorList)

def BFS_ST(graph, start):
    visited = set([start])
    queue = cols.deque([start])
    while queue:
        v = queue.popleft()
        nbr = graph[v] - visited
        for u in nbr:
            print("(", v, ",", u, ")", end = '')
            visited.add(u)
            queue.append(u)

def Topological_sort_AM(vertex, graph):
    n = len(vertex)
    inDeg = [0]*n

    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                inDeg[j] += 1

    vlist = []
    for i in range(n):
        if inDeg[i] == 0:
            vlist.append(i)

    while len(vlist) > 0:
        v= vlist.pop()
        print(vertex[v], end =' ')

        for u in range(n):
            if v!= u and graph[v][u] > 0:
                inDeg[u] -= 1
                if inDeg[u] == 0:
                    vlist.append(u)

vertex = ['A','B','C','D','E','F']
graphAM = [[0,0,1,1,0,0],
           [0,0,0,1,1,0],
           [0,0,0,1,0,1],
           [0,0,0,0,0,1],
           [0,0,0,0,0,1],
           [0,0,0,0,0,0]]
print('topological_sort: ')
Topological_sort_AM(vertex, graphAM)
print()
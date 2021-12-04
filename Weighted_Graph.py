vertex = ['A','B','C','D','E','F','G','H']
adjMat = [[None,29,3,None,None,None,None,None],
          [29,None,None,5,None,None,None,None],
          [3,None,None,14,8,None,None,None],
          [None,5,14,None,None,34,None,None],
          [None,None,8,None,None,None,4,9],
          [None,None,None,34,None,None,None,None],
          [None,None,None,None,4,None,None,13],
          [None,None,None,None,9,None,13,None]]

my_graph = {'A':{('B', 29), ('C', 3)},
             'B':{('A',29), ('D', 5)},
             'C':{('A', 3), ('D', 14), ('E', 8)},
             'D':{('B', 5), ('C', 14), ('F', 34)},
             'E':{('C', 8), ('G', 4), ('H', 9)},
             'F':{('D', 34)},
             'G':{('E', 4), ('H', 13)},
             'H':{('E', 9), ('G', 13)}}

def Weight_Adj_Sum(vlist, adj):
    sum = 0
    num = len(vlist)
    for i in range(num):
        for j in range(i + 1, num):
            if adj[i][j] != None:
                sum += adj[i][j]
    return sum

def Print_Adj_AllEdges(vlist, adj):
    num = len(vlist)
    for i in range(num):
        for j in range(i + 1, num):
            if adj[i][j] != None:
                print("(%s,%s,%d)"%(vlist[i],vlist[j],adj[i][j]), end = '')
    print()

def Weight_List_Sum(vlist, graph):
    sum = 0
    for v in graph:
        for e in graph[v]:
            sum += e[1]
    return sum // 2

def Print_List_AllEdges(vlist, graph):
    for v in graph:
        for e in graph[v]:
            print("(%s,%s,%d)"%(v,e[0],e[1]), end = ' ')

print("Weight Sum : ", Weight_Adj_Sum(vertex, adjMat))
Print_Adj_AllEdges(vertex, adjMat)
print("Weight Sum : ", Weight_List_Sum(vertex, my_graph))
Print_List_AllEdges(vertex, my_graph)
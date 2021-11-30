####################
# 프로그래밍 숙제 #4 #
####################

############
# DFS 함수 #
############
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # 좌표 상하좌우 움직임

def DFS(x, y, num):
    global width, my_graph
    if x > -1 and x < n and y > -1 and y < n and my_graph[x][y] == num:     # 해당 위치가 배열을 벗어나는지, 인접배열과 숫자가 일치하는지
        width += 1
        my_graph[x][y] = 0
        for i in move:  # 상하좌우 이동
            x += i[0]
            y += i[1]
            DFS(x, y, num)
            x -= i[0]
            y -= i[1]

########
# 실행 #
########

n = int(input("정방배열의 행과 열의 수를 입력하세요 : "))
my_graph=[]
print("배열을 입력하세요 :")
for i in range(n):
    my_graph.append(list(map(int, input().split())))

result = {}     # 결과 저장 딕셔너리 => {숫자 : [영역의 개수, 넓이]}
width = 0

for i in range(n):
    for j in range(n):
        if my_graph[i][j] != 0 :
            num = my_graph[i][j]
            if num in result:           # result에 num 값 존재하면
                result[num][0] += 1     # 해당 숫자의 영역 개수만 늘림
                DFS(i, j, num)
            else:
                result[num] = [1, 0]    # num 값 존재하지 않으면 num으로 새로운 키 생성 [영역 개수, 넓이]
                DFS(i, j, num)

            if result[num][1] < width:  # 깊이우선탐색 num의 영역 넓이가 기존의 넓이보다 크면
                result[num][1] = width

        width = 0

result = sorted(result.items())         # 딕셔너리 키 값 기준으로 정렬

print()
for i in result:
    print("숫자 :", i[0])
    print("영역의 개수 :", i[1][0])
    print("최대 넓이 :", i[1][1])
    print()


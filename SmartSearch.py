import PriorityQueueByPython as PQ
import math
map = [['1','1','1','1','1','1'],
       ['e','0','0','0','0','1'],
       ['1','0','1','0','1','1'],
       ['1','1','1','0','0','x'],
       ['1','1','1','0','1','1'],
       ['1','1','1','1','1','1']]
MAZE_SIZE = 6

class NewPriorityQueue(PQ.PriorityQueue):
    def FindMaxIndex(self):
        if self.isEmpty():
            return None
        else:
            highest = 0
            for i in range(1, self.Size()):
                if self.items[i][2] > self.items[highest][2]:
                    highest = i
            return highest


(ox,oy) = (5, 4)

def dist(x,y):
    global ox, oy
    (dx, dy) = (ox-x, oy-y)
    return math.sqrt(dx*dx + dy*dy)

def isValidPos(x, y):
    global MAZE_SIZE
    if x < 0 or y < 0 or x >=MAZE_SIZE or y >= MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0'  or map[y][x] == 'x'

def MySmartSearch():
    q = NewPriorityQueue()
    q.Enqueue((0, 1, -dist(0, 1)))
    print('PQueue: ')

    while not q.isEmpty():
        here = q.Dequeue()
        print(here[0:2],end='->')
        x, y, _ = here
        if (map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y-1):
                q.Enqueue((x, y-1, -dist(x, y-1)))
            if isValidPos(x, y+1):
                q.Enqueue((x, y+1, -dist(x, y+1)))
            if isValidPos(x-1, y):
                q.Enqueue((x-1, y, -dist(x-1, y)))
            if isValidPos(x+1, y):
                q.Enqueue((x+1, y, -dist(x+1, y)))
        print('우선순위큐: ',q.items)
    return False

result = MySmartSearch()
if result:
    print(' --> 미로탐색 성공')
else:
    print(' --> 미로탐색 실패')
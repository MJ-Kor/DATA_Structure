import CircleQueueByPython      ### 모듈

class Circle_Deque (CircleQueueByPython.Circle_Queue):
    def __init__(self):
        super().__init__()

    def addFront(self, e):
        if self.isFull():
            print("덱이 가득 찼습니다.")
        else:
            self.CQueue[self.front] = e
            self.front-=1
            if self.front < 0:
                self.front += CircleQueueByPython.MAX_QSIZE

    def getFront(self):
        return self.Peek()

    def delFront(self):
        return self.deQueue()

    def addRear(self, e):
        self.enQueue(e)

    def getRear(self):
        if not self.isEmpty():
            return self.CQueue[self.rear]

    def delRear(self):
        if not self.isEmpty():
            self.rear -= 1
            if self.rear < 0:
                self.rear += CircleQueueByPython.MAX_QSIZE
            return self.CQueue[self.rear]

dq = Circle_Deque()
for i in range(9):
    if i % 2 == 0:
        dq.addRear(i)
    else:
        dq.addFront(i)
dq.Display()
for i in range(2):
    dq.delFront()
for i in range(3):
    dq.delRear()
dq.Display()
for i in range(9,14):
    dq.addFront(i)
dq.Display()
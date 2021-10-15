### 물리적으로는 선형이지만 논리적으로 원형으로 만들어준다.
### 선형큐와 달리 리스트의 크기가 고정되어야 한다.
### 맨 처음에는 FRONT = REAR = 0이다.
### 삽입연산은 REAR+1 하고 그 위치에 항목을 넣는 것.
### 삭제연산도 FRONT+1 하고 그 위치의 항목을 반환.
### 실제로는 정해진 크기보다 1 적게 저장 가능
### 아래는 크기가 8인 큐 ,

MAX_QSIZE = 10

class Circle_Queue:
    def __init__(self):
        self.CQueue = [None]*MAX_QSIZE
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        if self.rear == self.front:
            return True
        else:
            return False

    def isFull(self):
        if self.front == (self.rear + 1) % MAX_QSIZE:     ## FRONT가 REAR보다 하나 앞에 있을 경우.
            return True
        else:
            return False

    def enQueue(self, e):
        if self.isFull():
            print("큐가 가득 찼습니다.")
        else:
            self.rear = (self.rear + 1) % MAX_QSIZE
            self.CQueue[self.rear] = e

    def deQueue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % MAX_QSIZE
            return self.CQueue[self.front]

    def Peek(self):
        if not self.isEmpty():
            return self.CQueue[(self.front + 1) % MAX_QSIZE]

    def Display(self):
        out = []
        if self.rear < self.front:
            out = self.CQueue[self.front + 1 : MAX_QSIZE] + self.CQueue[0 : self.rear + 1]
        else:
            out = self.CQueue[self.front + 1 : self.rear + 1]
        print("[f = %s, r = %d] ==> "%(self.front, self.rear), out)
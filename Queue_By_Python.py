# 큐 : 선입선출 - 나가는 것은 앞으로 들어오는 것은 뒤로

class Queue:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = -1

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def enQueue(self, e):
        self.queue.append(e)

    def deQueue(self):
        if not self.isEmpty():
            return self.queue.pop(self.front)   # 여기서 맨 앞 원소를 꺼내고 모든 원소 앞으로 땡기기 때문에 O(N)

    def Peek(self):
        if not self.isEmpty():
            return self.queue[self.rear]

    def Size(self):
        return len(self.queue)

    def Clear(self):
        self.queue = []



    ###### 이런 선형 큐는 삭제할 때 시간 복잡도가 O(N)인 문제가 있다.
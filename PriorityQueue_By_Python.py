# 선형 큐로 구현

class PriorityQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def Size(self):
        return len(self.items)

    def Clear(self):
        self.items = []

    def Enqueue(self, e):
        self.items.append(e)

    def FindMaxIndex(self):
        if self.isEmpty():
            return None
        else:
            highest = 0
            for i in range(1, self.Size()):
                if self.items[i]>self.items[highest]:
                    highest = i
            return highest

    def Dequeue(self):
        highest = self.FindMaxIndex()
        if highest is not None:
            return self.items.pop(highest)

    def Peek(self):
        highest = self.FindMaxIndex()
        if highest is not None:
            return self.items[highest]


if __name__ == '__main__':
    q = PriorityQueue()
    q.Enqueue(34)
    q.Enqueue(18)
    q.Enqueue(27)
    q.Enqueue(45)
    q.Enqueue(15)

    print("PQueue", q.items)
    while not q.isEmpty():
        print("Max Priority = ",q.Dequeue())



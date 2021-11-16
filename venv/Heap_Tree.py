class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)

    def Size(self):
        return len(self.heap) - 1

    def IsEmpty(self):
        return self.Size() == 0

    def Parent(self, i):
        return self.heap[i // 2]

    def Left(self, i):
        return self.heap[2 * i]

    def Right(self, i):
        return self.heap[2 * i + 1]

    def Display(self, msg = '힙 트리 : '):
        print(msg, self.heap[1:])

    def Insert(self, n):
        self.heap.append(n)
        i = self.Size()
        while i != 1 and self.Parent(i) < n:
            self.heap[i] = self.Parent(i)
            i = i // 2
        self.heap[i] = n

    def Delete(self):
        parent = 1
        child = 2
        if not self.IsEmpty():
            hroot = self.heap[1]
            last = self.heap[self.Size()]
            while(child <= self.Size()):
                if child < self.Size() and self.Left(parent) < self.Right(parent):
                    child += 1
                if last >= self.heap[child]:
                    break
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2
            self.heap[parent] = last
            self.heap.pop(-1)
            return hroot

heap = MaxHeap()
data = [2, 5, 4, 8, 9, 3, 7, 3]
print("[삽입 연산] : ", data)
for elem in data:
    heap.Insert(elem)
heap.Display('[ 삽입 후 ] : ')
heap.Delete()
heap.Display('[ 삭제 후 ] : ')
heap.Delete()
heap.Display('[ 삭제 후 ] : ')

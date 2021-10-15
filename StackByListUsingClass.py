class Stack:
    def __init__(self):
        self.top=[]

    def IsEmpty(self):
        return len(self.top) == 0

    def Push(self, item):
        self.top.append(item)  # 맨 뒤에 추가 할 경우 맨 앞에 할 때보다 시간 복잡도 이득

    def Pop(self):
        if not self.IsEmpty():
            return self.top.pop(-1)

    def Peek(self):
        if not self.IsEmpty():
            return self.top[-1]

    def Size(self):
        return len(self.top)

    def clear(self):
        self.top = []


odd = Stack()
even = Stack()
for i in range(10):
    if i % 2 == 0 : even.push(i)
    else : odd.push(i)

print(' 스택 even push 5회', even.top)
print(' 스택 odd push 5회',odd.top)
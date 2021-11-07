class Node:
    def __init__(self, e, link = None):
        self.data = e
        self.link = link

class LinkedStack:
    def __init__(self):
        self.top = None
        self.count = 0
    def Clear(self):
        self.top = None

    def isEmpty(self):
        return self.top == None

    def Push(self, e):
        n = Node(e, self.top)
        self.top = n
        self.count += 1

    def Pop(self):
        if not self.isEmpty():
            n = self.top
            self.top = n.link
            self.count -= 1
            return n.data               # 자연스럽게 메모리 반환

    def Peek(self):
        return self.top.data

    def Size(self):
        # count = 0
        # n = self.top
        # while n != None:
        #     count+=1
        #     n = n.link
        return self.count

    def Display(self, msg = 'Linked Stack:'):
        print(msg, end = ' ')
        n = self.top
        while n != None:
            print(n.data, end = ' ')
            n = n.link
        print()


odd = LinkedStack()
even = LinkedStack()
for i in range(10):
    if i % 2 == 0 : even.Push(i)
    else : odd.Push(i)

odd.Display()
even.Display()

print(odd.Size())




class DNode:
    def __init__(self, e, prev = None, next = None):
        self.data = e
        self.prev = prev
        self.next = next

class DoublyLinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None

    def Clear(self):
        self.front = None
        self.rear = None

    def Size(self):
        if not self.isEmpty():
            node = self.front
            count = 1
            while not node == None:
                node = node.next
        else:
            return 0

    def Display(self, msg = "Doubly Linked List: "):
        print(msg, end = '')
        node = self.front
        while node != None:
            print(node.data, end =' ')
            node = node.next
        print()


    def addFront(self, e):
        node = DNode(e, None, self.front)
        if self.isEmpty():
            self.front = node
            self.rear = node
        else:
            self.front.prev = node
            self.front = node

    def addRear(self, e):
        node = DNode(e, self.rear, None)
        if self.isEmpty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def deleteFront(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear == None
            else:
                self.front.prev = None
            return data

    def deleteRear(self):
        if not self.isEmpty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:
                self.front == None
            else:
                self.rear.next = None
            return data

dq = DoublyLinkedDeque()
for i in range(9):
    if i % 2 == 0:
        dq.addRear(i)
    else:
        dq.addFront(i)
dq.Display()
for i in range(2):
    dq.deleteFront()
for i in range(3):
    dq.deleteRear()
dq.Display()
for i in range(9,14):
    dq.addFront(i)
dq.Display()


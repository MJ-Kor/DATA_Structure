class Node:
    def __init__(self, e, Link = None):
        self.data = e
        self.link = Link

class CircularLinkedQueue:
    def __init__(self):
        self.tail = None

    def isEmpty(self):
        return self.tail == None

    def clear(self):
        self.tail = None

    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data

    def Enqueue(self, e):
        node = Node(e)
        if self.isEmpty():
            node.link = node
            self.tail = node
        else:
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node

    def Dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail.link == self.tail:
                self.tail == None
            else:
                self.tail.link = self.tail.link.link
            return data

    def Size(self):
        if self.isEmpty():
            return 0
        else:
            count = 1
            node = self.tail.link
            while not node == self.tail:
                node = node.link
                count +=1
            return count

    def Display(self, msg = "CircularLinkedQueue: "):
        print(msg, end = '')
        if not self.isEmpty():
            node = self.tail.link
            while not node == self.tail:
                print(node.data, end = ' ')
                node = node.link
            print(node.data, end = ' ')
        print()

q = CircularLinkedQueue()
q.Enqueue(0) ;  q.Enqueue(1) ;  q.Enqueue(2) ;  q.Enqueue(3) ;  q.Enqueue(4) ;  q.Enqueue(5)
q.Enqueue(6) ;  q.Enqueue(7)
q.Display()
q.Dequeue() ;  q.Dequeue() ;  q.Dequeue() ;  q.Dequeue() ;  q.Dequeue()
q.Display()
q.Enqueue(8) ;  q.Enqueue(9);  q.Enqueue(10) ;  q.Enqueue(11) ;  q.Enqueue(12) ;  q.Enqueue(13)
q.Display()

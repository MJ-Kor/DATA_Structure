class Node:
    def __init__(self, e, Link = None):
        self.data = e
        self.link = Link

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def Clear(self):
        self.head = None

    def Size(self):
        count = 0
        n = self.head
        while n != None:
            count+=1
            n = n.link

        return count

    def Display(self, msg = 'Linked List:'):
        print(msg, end = ' ')
        n = self.head
        while n != None:
            print(n.data, end = '->')
            n = n.link
        print(None)

    def getNode(self, pos):             # n번째 노드 찾아감
        if pos < 0:
            return None
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node

    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            return node.data

    def Replace(self, pos, e):
        node = self.getNode(pos)
        if node != None:
            node.data = e

    def Find(self, e):
        node = self.head
        while node != None:
            if node.data == e:
                return node
            node = node.link
        return None

    def Insert(self, pos, e):
        before = self.getNode(pos-1)
        if before == None:
            self.head = Node(e, self.head)
        else:
            node = Node(e, before.link)
            before.link = node

    def Delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            if self.head != None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link

s = LinkedList()
s.Display("단순연결리스트로 구현한 리스트(초기상태):")
s.Insert(0, 10);    s.Insert(0, 20);    s.Insert(1, 30);
s.Insert(s.Size(), 40);     s.Insert(2, 50);
s.Display("단순연결리스트로 구현한 리스트 (삽입X5)")
s.Replace(2, 90)
s.Display("단순연결리스트로 구현한 리스트 (교체X1)")
s.Delete(2);    s.Delete(s.Size()-1);   s.Delete(0);
s.Display("단순연결리스트로 구현한 리스트 (삭제X3)")
s.Clear()
s.Display("단순연결리스트로 구현한 리스트 (정리 후)")


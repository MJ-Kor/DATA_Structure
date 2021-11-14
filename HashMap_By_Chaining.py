class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str("%s:%s"%(self.key, self.value))

class Node:
    def __init__(self, e, Link = None):
        self.data = e
        self.link = Link


class HashChainMap:
    def __init__(self, M):
        self.table = [None] * M
        self.M = M

    def HashFn(self, key):
        sum = 0
        for c in key:
            sum = sum + ord(c)
        return sum % self.M                 # 제산 함수

    def Insert(self, key, value):
        idx = self.HashFn(key)
        self.table[idx] = Node(Entry(key, value), self.table[idx])

    def Search(self, key):
        idx = self.HashFn(key)
        node = self.table[idx]
        while node is not None:
            if node.data.key == key:
                return node.data
            node = node.link
        return None

    def Delete(self, key):
        idx = self.HashFn(key)
        node = self.table[idx]
        before = None
        while node is not None:
            if node.data.key == key:
                if before == None:
                    self.table[idx] = node.link
                else:
                    before.link = node.link
                return
            before = node
            node = node.link

    def Display(self, msg):
        print(msg)
        for idx in range(len(self.table)):
            node = self.table[idx]
            if node is not None:
                print("[%2d] -> "%idx, end = '')
                while node is not None:
                    print(node.data, end = ' -> ')
                    node = node.link
                print()

map = HashChainMap(13)
map.Insert('data', '자료')
map.Insert('structure', '구조')
map.Insert('sequential search', '순차 탐색')
map.Insert('game', '게임')
map.Insert('binary search', '이진 탐색')

# 7번 위치에서 두번의 충돌이 일어남

map.Display("나의 단어장 : ")

print("탐색 : game -> ", map.Search('game'))
print("탐색 : over -> ", map.Search('over'))
print("탐색 : data -> ", map.Search('data'))

map.Delete('game')
map.Display("나의 단어장 : ")


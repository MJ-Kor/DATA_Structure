class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str("%s:%s"%(self.key, self.value))

def Sequential_Search(A, key, low, high):
    for i in range(low, high + 1):
        if A[i].key == key:
            return i
    return None

class SequentialMap:
    def __init__(self):
        self.table = []

    def Size(self):
        return len(self.table)

    def Display(self, msg):
        print(msg)
        for entry in self.table:
            print(" ", entry)

    def Insert(self, key, value):
        self.table.append(Entry(key, value))

    def Search(self, key):
        pos = Sequential_Search(self.table, key, 0, self.Size()-1)
        if pos is not None:
            return self.table[pos]
        else:
            return None

    def Delete(self, key):
        for i in range(self.Size()):
            if self.table[i].key == key:
                self.table.pop(i)
                return

map = SequentialMap()
map.Insert('data', '자료')
map.Insert('structure', '구조')
map.Insert('sequential search', '순차 탐색')
map.Insert('game', '게임')
map.Insert('binary search', '이진 탐색')

map.Display("나의 단어장 : ")

print("탐색 : game -> ", map.Search('game'))
print("탐색 : over -> ", map.Search('over'))
print("탐색 : data -> ", map.Search('data'))

map.Delete('game')
map.Display("나의 단어장 : ")

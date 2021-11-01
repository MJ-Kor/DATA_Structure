class ArrayList:
    def __init__(self):
        self.items = []

    def Insert(self, pos, e):
        self.items.insert(pos, e)

    def Delete(self, pos):
        return self.items.pop(pos)

    def IsEmpty(self):
        if len(self) == 0:
            return True
        else:
            return False

    def GetEntry(self, pos):
        return self.items[pos]

    def Size(self):
        return len(self.items)

    def Clear(self):
        self.items.clear()
        # 아니면
        # self.items = []

    def Find(self, item):
        return self.items.index(item)

    def Replace(self, pos, item):
        self.items[pos] = item

    def Sort(self):
        self.items.sort()

    def Merge(self, lst):
        self.items.extend(lst)

    def Display(self, msg="ArrayList"):
        print(msg, self.Size(), self.items)

    def Append(self, e):
        self.items.append(e)


s = ArrayList()
s.Display('파이썬 클래스 리스트로 구현한 리스트 테스트:')
s.Insert(0,10);s.Insert(0,20);s.Insert(1,30);s.Insert(s.Size(),40);s.Insert(2,50)
s.Display('데이터 삽입x5:')
s.Sort()
s.Display('리스트 정렬:')
s.Replace(2,90)
s.Display('데이터 변경:')
s.Delete(2);s.Delete(s.Size()-1);s.Delete(0)
s.Display('데이터 삭제:')
lst = [1,2,3]
s.Merge(lst)
s.Display('리스트 합병:')
s.Clear()
s.Display('리스트 정리:')

# 시간 복잡도는 그냥 함수 구현과 똑같다
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

def myLineEditor():
    list = ArrayList()
    while True:
        command = input("[메뉴선택] i-입력,d-삭제,r-변경,p-출력,l-파일읽기,s-저장,q-종료=>")
        if command == 'i':
            pos = int(input("입력행 번호: "))
            str = input("내용: ")
            list.Insert(pos,str)
        elif command == 'd':
            pos = int(input("삭제행 번호: "))
            list.Delete(pos)
        elif command == 'r':
            pos = int(input("변경행 번호: "))
            str = input("변경내용: ")
            list.Replace(pos,str)
        elif command == 'p':
            print("Line Editor")
            for line in range(list.Size()):
                print("[%2d]"%line, end='')
                print(list.GetEntry(line))
        elif command == 'l':
            filename='test.txt'
            infile = open(filename,"r")
            lines = infile.readlines()
            for line in lines:
                list.Insert(list.Size(),line.rstrip('\n'))
            infile.close()
        elif command == 's':
            filename = 'test.txt'
            outfile = open(filename, "w")
            for i in range(list.Size()):
                outfile.write(list.GetEntry(i)+'\n')
            outfile.close()
        elif command == 'q':
            return

myLineEditor()
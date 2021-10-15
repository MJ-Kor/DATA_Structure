# mf = input("괄호가 들어간 문장을 입력하세요. : ")

class Stack:
    def __init__(self):
        self.top = []

    def IsEmpty(self):
        return len(self.top) == 0

    def Size(self):
        return len(self.top)

    def Push(self,e):
        self.top.append(e)

    def Pop(self):
        if not self.IsEmpty():
            return self.top.pop(-1)

    def Peek(self):
        if not self.IsEmpty():
            return self.top[-1]

    def Clean(self):
        self.top = []

def Bracket_Check(str):
    stack = Stack()
    for i in list(str):
        if i in ('(','{','['):
            stack.Push(i)
        elif i in (')','}',']'):
            if stack.IsEmpty():
                return False
            else:
                left = stack.Pop()
                if (left == '(' and i !=')') or (left == '[' and i !=']') or (left == '{' and i !='}'):
                    return False

    return stack.IsEmpty()


filename = "ArrayStackk.txt"
infile = open(filename,'r')
lines = infile.readlines()
infile.close()

result = Bracket_Check(lines)
print(result)
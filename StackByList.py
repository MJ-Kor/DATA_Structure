top=[]

def IsEmpty():
    return len(top) == 0
def Push(item):
    top.append(item) # 맨 뒤에 추가 할 경우 맨 앞에 할 때보다 시간 복잡도 이득
def Pop():
    if not IsEmpty():
        return top.pop(-1)
def Peek():
    if not IsEmpty():
        return top[-1]
def Size():
    return len(top)
def clear():
    global top
    top = []

for i in range(1,6):
    Push(i)
print("push 5회",top)
print("pop() --> ", Pop())
print("pop() --> ", Pop())
print("pop 2회",top)


class Stack:  # 스택 클래스
    def __init__(self):
        self.top = []

    def IsEmpty(self):
        return len(self.top) == 0

    def Push(self, e):
        self.top.append(e)

    def Pop(self):
        if not self.IsEmpty():
            return self.top.pop(-1)

    def Peek(self):
        if not self.IsEmpty():
            return self.top[-1]

    def Size(self):
        return len(self.top)

    def Clean(self):
        self.top = []

def Check_Palindrome(cknum):                    # Palindrome 확인 함수
    stack = Stack()
    half = len(cknum)//2
    i = 0
    while i < len(cknum):
        if i<half:
            stack.Push(cknum[i])
        else:
            if (len(cknum) % 2) != 0 and i == half:     # 길이가 홀수인 숫자의 중앙에 위치한 수는 제외
                pass
            else :
                left = stack.Pop()
                if cknum[i] != left:
                    return False
        i+=1
    return True
def Change_num(chnum):                          # 숫자 뒤집기
    revnum = list(chnum)
    revnum.reverse()
    resnum = int(chnum) + int(''.join(revnum))
    return str(resnum)

recursive_num = 0                               # 순환 횟수

def Make_Palindrome(mknum):
    global recursive_num
    if Check_Palindrome(mknum):                 # Palindrome 이라면 해당 숫자와 순환 횟수 출력
        print("Palindrome :", mknum)
        print("Recursive num:", recursive_num)
    else:
        recursive_num += 1
        Make_Palindrome(Change_num(mknum))


a = input("양의 정수를 입력하세요 : ")
Make_Palindrome(a)


import StackByListUsingClass as sc
import Postfix_By_Stack as ps

infix1 = ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']

def Precedence(op):
    if op == '(' or op ==')':
        return 0
    elif op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    else:
        return -1

def InToPost(exrp):
    ITP = sc.Stack()
    output = []
    for ch in exrp:
        if ch == '(':
            ITP.Push(ch)
        elif ch == ')':
            while not ITP.IsEmpty():
                op = ITP.Pop()
                if op == '(':
                    break
                else:
                    output.append(op)
        elif ch in "+-*/":
            while not ITP.IsEmpty():
                op = ITP.Peek()
                if (Precedence(op) >= Precedence(ch)):
                    output.append(op)
                    ITP.Pop()
                else:
                    break
            ITP.Push(ch)
        else:
            output.append(ch)
    while not ITP.IsEmpty():
        output.append(ITP.Pop())
    return output

print("중위 표기: ", infix1)
print("후위 표기: ", InToPost(infix1))
print("연산 결과: ", ps.Postfix(InToPost(infix1)))
import StackByListUsingClass as sc

expr1 = ['8', '2', '/', '3', '-', '3', '2', '*', '+']

def Postfix(expr):
    psc = sc.Stack()
    for ch in expr:
        if ch in "+-/*":                # 연산자 만나면 바로 스택에서 두 개 꺼내서 계산 후 다시 저장
            val2 = psc.Pop()
            val1 = psc.Pop()
            if ch == '+':
                psc.Push(val1 + val2)
            elif ch == '-':
                psc.Push(val1 - val2)
            elif ch == '*':
                psc.Push(val1 * val2)
            elif ch == '/':
                psc.Push(val1 / val2)
        else:
            psc.Push(float(ch))

    return psc.Pop()

if __name__ == '__main__':
    print(expr1, '-->', Postfix(expr1))
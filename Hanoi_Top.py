def Hanoi(n, fr, tmp, to):
    if n == 1:
        print('원판 1 : %s --> %s'%(fr, to))
    else:
        Hanoi(n-1, fr, to, tmp)
        print('원판 %d : %s --> %s'%(n, fr, to))
        Hanoi(n-1, tmp, fr, to)

Hanoi(4, 'A', 'B', 'C')
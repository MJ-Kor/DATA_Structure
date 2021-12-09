def sortGapInsertion(A, first, last, gap):
    for i in range(first+gap, last+1, gap):
        key = A[i]                              # 부분 리스트에서 왼쪽부터 확인 후
        j = i-gap
        while j >= first and key < A[j]:        # 다시 정렬한다.
            A[j + gap] = A[j]
            j = j-gap
        A[j + gap] = key

def Shell_sort(A):
    n = len(A)
    gap = n//2
    while gap > 0:
        if gap % 2 == 0:
            gap += 1
        for i in range(gap):
            sortGapInsertion(A, i, n - 1, gap)
        print('    Gap =', gap, A)
        gap = gap // 2


A = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print(A)
Shell_sort(A)
print(A)
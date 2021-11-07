# 선택 정렬
# 가장 작은 숫자를 선택해서 앞쪽으로 옮기는 방법
# O(n^2), 안정성 만족하지 않음

def PrintStep(arr, val):
    print(" Step %2d = " % val, end = '')
    print(arr)

def Selection_sort(a):
    n = len(a)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if (a[j] < a[least]):
                least = j
        a[i], a[least] = a[least], a[i]         # 파이썬은 바로 교환 가능, 새로운 리스트 하나 안만들어도 된다. => 제자리 정렬
        PrintStep(a, i + 1)

data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("Original :", data)
Selection_sort(data)
print("Selection: ", data)
# 버블 정렬(비교 - 교환)
# 한 번의 스캔(처음부터 끝까지 비교 - 교환)에 가장 큰 레코드가 오른쪽 끝으로 배치
# 안정성 만족

def PrintStep(arr, val):
    print(" Step %2d = " % val, end = '')
    print(arr)

def Bubble_sort(a):
    n = len(a)
    for i in range(n-1, 0, -1):
        bChanged = False
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                bChanged = True
        if not bChanged:
            break
        PrintStep(a, n - i)


data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("Original :", data)
Bubble_sort(data)
print("Bubble: ", data)
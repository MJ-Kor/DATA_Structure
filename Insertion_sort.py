# 삽입 정렬
# 끼워넣어가며 정렬, 그러면 자연스럽게 끼워지는 위치 이후의 것은 뒤로 밀어짐
# 최선(정렬되어 있는 경우) : O(n), 최악(역으로 정렬되어 있는 경우) : O(n^2)
# 안정성 만족
# 많은 레코드들의 이동이 필요해 자료가 방대할 경우 효율 x
# 대부분의 레코드가 이미 정렬되어 있는 경우 효율

def PrintStep(arr, val):
    print(" Step %2d = " % val, end = '')
    print(arr)

def Insertion_sort(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j = i-1
        while j >= 0 and a[j] > key :
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        PrintStep(a,i)

data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("Original :", data)
Insertion_sort(data)
print("Insertion: ", data)
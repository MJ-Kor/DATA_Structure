def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l<n and arr[l]>arr[i]:
        largest = l
    if r<n and arr[r]>arr[largest]:
        largest = r
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n , largest)

def Inplace_sort(arr):
    n = len(arr)
    print('i = ', 0, arr)
    for i in range(n//2, -1 , -1):
        heapify(arr, n, i)
        print("i = ", i , arr)
    print()
    for i in range(n-1, 0, -1):             # 최대 힙을 바로 정렬하기 for 구문 범위 -> 최대 값 꺼내서 정렬하면 그 부분은 제외하고 heapify
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i ,0)
        print("i = ", i, arr)

A = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print(A)
Inplace_sort(A)
print(A)
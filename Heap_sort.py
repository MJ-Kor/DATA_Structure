import Heap_Tree as HT

def Heap_sort(data):
    heap = HT.MaxHeap()
    for i in data:
        heap.Insert(i)

    for i in range(1, len(data) + 1):
        data[-i] = heap.Delete()

A = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print(A)
Heap_sort(A)
print(A)
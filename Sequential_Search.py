# 최악 : O(n)
# 최선 : O(1)

def Sequential_Search(A, key, low, high):
    for i in range(low, high + 1):
        if A[i].key == key:
            return i
    return None


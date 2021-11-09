# 이진 탐색을 사용하려면 배열이 정렬되어 있어야 함
# 시간복잡도 : O(logN)


def Binary_Search(A, low, key, high):
    if(low <= high):                        # 항목이 남아있는 경우
        middle = (low + high) // 2
        if key == A[middle].key:
            return middle
        elif key < A[middle]:
            return Binary_Search(A, low, key, middle - 1)       # 왼쪽 부분리스트 탐색
        else:
            return Binary_Search(A, middle + 1, key, high)      # 오른쪽 부분리스트 탐색
    else:
        return None
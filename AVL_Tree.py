# AVL 트리
# 모든 노드에서 왼쪽 서브트리와 오른쪽 서브트리의 높이 차가 1을 넘지 않는 이진탐색트리
# 모든 노드의 균형 인수는 0이나 +-1이 되어야 한다.
# 이진탐색트리의 조건을 만족한다.

# N : 새로 추가되는 노드, A : 노드 삽입으로 인해 균형이 깨지는 가장 가까운 노드
# LL 타입 : N이 A의 왼쪽 자식의 왼쪽 서브 트리에 삽입
# RR 타입 : N이 A의 오른쪽 자식의 오른쪽 서브 트리에 삽입
# LR 타입 : N이 A의 왼쪽 자식의 오른쪽 서브 트리에 삽입
# RL 타입 : N이 A의 오른쪽 자식의 왼쪽 서브 트리에 삽입

# LL 회전 : 회전하면서 A의 왼쪽 자식 노드의 오른쪽 서브트리가 A의 오른쪽 자식노드로 들어감
def rotateLL(A):
    B = A.left
    A.left = B.right
    B.right = A
    return B        # 새로운 루트 반환

# RR 회전 : 회전하면서 A의 오른쪽 자식 노드의 왼쪽 서브트리가 A의 왼쪽 자식노드로 들어감
def rotateRR(A):
    B = A.right
    A.right = B.left
    B.left = A
    return B        # 새로운 루트 반환

# RL 회전 : 불균형이 일어난 노드를 기준으로 오른쪽 자식노드에 LL회전이 일어나고 그 뒤 불균형 일어난 노드에 RR회전을 해줌
def rotateRL(A):
    B = A.right
    A.right = rotateLL(B)
    return rotateRR(A)

# LR 회전 : 불균형이 일어난 노드를 기준으로 왼쪽 자식노드에 RR회전이 일어나고 그 뒤 불균형 일어난 노드에 LL회전을 해줌
def rotateLR(A):
    B = A.left
    A.left = rotateRR(B)
    return rotateLL(A)

# 트리 높이
def Calc_height(n):
    if n is None:
        return 0
    hleft = Calc_height(n.left)
    hright = Calc_height(n.right)
    if hleft > hright:
        return hleft + 1
    else:
        return hright + 1

# 트리 높이 차 반환 함수
def Calc_height_diff(n):
    if n is None:
        return 0
    hleft = Calc_height(n.left)
    hright = Calc_height(n.right)
    return hleft - hright

# 재균형 함수
def Rebalance(parent):
    hDiff = Calc_height_diff(parent)
    if hDiff > 1:
        if Calc_height_diff(parent.left) > 0:
            parent = rotateLL(parent)
        else:
            parent = rotateLR(parent)
    elif hDiff < -1:
        if Calc_height_diff(parent.right) < 0:
            parent = rotateRR(parent)
        else:
            parent = rotateRL(parent)
    return parent

# 삽입 함수
# 이진탐색트리의 삽입과 다른점
# 1. 항상 삽입하고 재균형인지 확인
# 2. 삽입 후 루트가 달라질 수 있으므로 루트 반환
def Insert_Avl(parent, node):
    if node.key < parent.key:
        if parent.left != None:
            parent.left = Insert_Avl(parent.left, node)
        else:
            parent.left = node
        return Rebalance(parent)
    elif node.key > parent.key:
        if parent.right != None:
            parent.right = Insert_Avl(parent.right, node)
        else:
            parent.right = node
        return Rebalance(parent)
    else:
        print("중복된 키 에러")
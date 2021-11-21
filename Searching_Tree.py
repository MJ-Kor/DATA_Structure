class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

def search_bst(n, key):                 # 순환함수
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)

def search_bst_iter(n, key):            # 반복함수
    while n is not None:
        if key < n.key:
            n = n.left
        elif key > n.key:
            n = n.right
        else:
            return n
    return None

def search_value_bst(n, value):         # 전위함수를 사용한 값에 의한 탐색
    if n == None:
        return None
    elif n.value == value:
        return n
    res = search_value_bst(n.left, value)
    if res is not None:
        return n
    else:
        return search_value_bst(n.right, value)

def search_max_bst(n):
    while n != None and n.right != None:
        n = n.right
    return n

def search_min_bst(n):
    while n != None and n.left != None:
        n = n.left
    return n

def insert_bst(r, n):
    if n.key < r.key:
        if r.left is None:
            r.left = n
            return True
        else:
            return insert_bst(r.left, n)
    elif n.key > r.key:
        if r.right is None:
            r.right = n
            return True
        else:
            return insert_bst(r.right, n)
    else:
        return False

def delete_bst_case1(parent, node, root):       # 단말 노드의 삭제
    if parent is None:
        root = None
    else:
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None
    return root

def delete_bst_case2(parent, node, root):      # 한 쪽의 자식만 가진 노드의 삭제
    if node.left is not None:
        child = node.left
    else:
        child = node.right

    if node == root:
        root = child
    else:
        if node is parent.left:
            parent.left = child
        else:
            parent.right = child
    return root

def delete_bst_case3(parent, node, root):       # 양 쪽의 자식을 가지고 후계자가 오른쪽 서브트리의 최소 값일 경우
    succp = node
    succ = node.right
    while(succ.left != None):
        succp = succ
        succ = succ.left
    if (succp.left == succ):
        succp.left = succ.right
    else:
        succp.right = succ.right
    node.key = succ.key
    node.value = succ.value
    node = succ
    return root

def delete_bst(root, key):
    if root == None:
        return None
    parent = None
    node = root
    while node != None and node.key != key:
        parent = node
        if key < node.key:
            node = node.left
        else:
            node = node.right

    if node == None:
        return None
    if node.left == None and node.right == None:
        root = delete_bst_case1(parent, node, root)
    elif node.left == None or node.right == None:
        root = delete_bst_case2(parent, node, root)
    else:
        root = delete_bst_case3(parent, node, root)

    return root
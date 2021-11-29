####################
# 프로그래밍 숙제 #3 #
####################
import copy     # 깊은 복사 위한 copy

SetList = []    # 중위순환 집합 원소 저장

#######################
# 이진탐색트리 관련 함수 #
#######################

class BSTNode:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def search_bst(root, key):
    if root == None:
        return "F"
    elif key == root.key:
        return "T"
    elif key < root.key:
        return search_bst(root.left, key)
    else:
        return search_bst(root.right, key)

def insert_bst(root, node):
    if node.key < root.key:
        if root.left is None:
            root.left = node
            print("원소", node.key, "추가 성공.", end = ' ')
        else:
            insert_bst(root.left, node)
    elif node.key > root.key:
        if root.right is None:
            root.right = node
            print("원소", node.key, "추가 성공.", end = ' ')
        else:
            insert_bst(root.right, node)
    else:
        print("원소", node.key, "추가 실패(중복).", end = ' ')

def delete_bst_case1(parent, node, root):
    if parent is None:
        root = None
    else:
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None
    return root

def delete_bst_case2(parent, node, root):
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

def delete_bst_case3(parent, node, root):
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

def Pre_order(node):
    if node is not None:
        print(node.key, end = ' ')
        Pre_order(node.left)
        Pre_order(node.right)

def In_order(node):
    global SetList
    if node is not None:
        In_order(node.left)
        SetList.append(node.key)
        In_order(node.right)

def Level(root, key):
    sum = 0
    while root is not None:
        if key < root.key:
            root = root.left
            sum += 1
        elif key > root.key:
            root = root.right
            sum += 1
        else:
            return sum + 1
    return sum

def Calc_height(root):
    if root is None:
        return 0
    hleft = Calc_height(root.left)
    hright = Calc_height(root.right)
    if hleft > hright:
        return hleft + 1
    else:
        return hright + 1

#####################
# 집합의 그 외 기능들 #
#####################

def Preorder_Traverse(Set):
    if Set.root != None:
        print("집합", Set, "의 전위순회: ", end = ' ')
        Pre_order(Set.root)
        print()
    else:
        print("집합", Set, "은(는) 공집합입니다.")

def Level_Sum(Set, level):
    sum = 0
    tree_height = Calc_height(Set.root)
    if tree_height >= level:
        In_order(Set.root)
        for i in SetList:
            if Level(Set.root, i) == level:
                sum += i
        print("집합", Set, "의", level, "레벨 원소들의 합은", sum, "입니다.")
        SetList.clear()
    else:
        print("집합", Set, "의 이진탐색트리 최대 레벨은", tree_height, "입니다.")

def Inorder_nth(Set, num):
    global SetList
    In_order(Set.root)
    try:
        print("집합", Set, "의 중위순회", num, "번째 원소 :", SetList[num-1])
    except IndexError:
        print("집합", Set, "의 중위순회", num, "번째 원소는 존재하지 않습니다.")
    SetList = []

##############
# 집합 클래스 #
##############

class BSTSet:
    def __init__(self, name):
        self.Name = name
        self.root = None
        print("집합", self.Name, "생성.")
    def __str__(self):
        return "%s"%self.Name

    def Add(self, key):
        node = BSTNode(key)
        if self.IsEmpty() == "T":
            print("원소", key, "추가 성공.", end = ' ')
            self.root = node
        else:
            return insert_bst(self.root, node)

    def Search(self, key):
        if self.IsEmpty() == "T":
            print("집합", self.Name, "은(는) 공집합입니다.")
        else:
            result = search_bst(self.root, key)
            if result == "T":
                print("원소", key,"은(는) 집합", self.Name, "에 존재합니다.")
            else:
                print("원소", key, "은(는) 집합", self.Name, "에 존재하지 않습니다.")

    def Union(self, SetB):
        global SetList
        SetC = BSTSet(self.Name + "+" + SetB.Name)
        SetC.root = copy.deepcopy(self.root)
        In_order(SetB.root)
        if SetList != None:
            for i in SetList:
                SetC.Add(i)                 # 중위순환으로 원소 파악 후 합
        SetList.clear()
        return SetC

    def Difference(self, SetB):
        global SetList
        SetC = BSTSet(self.Name + "-" + SetB.Name)
        SetC.root = copy.deepcopy(self.root)
        In_order(SetB.root)
        if SetList != None:
            for i in SetList:
                delete_bst(SetC.root, i)    # 중위순환으로 원소 파악 후 차
        SetList.clear()
        return SetC

    def IsEmpty(self):
        if self.root == None:
            return "T"
        else:
            return "F"

dataA = [2, -6, 14, 9, 9, -1, -3, -5, 0]
dataB = [-1, 3, 9, -1, 8, 5, 2, 0]

########
# 실행 #
########

A = BSTSet("A")
for i in dataA:
    A.Add(i)

print()
print()

B = BSTSet("B")
for j in dataB:
    B.Add(j)

print()
print()

C = A.Union(B)
C.Name = "C"

print()
print()

D = A.Difference(B)
D.Name = "D"

print()

E = C.Difference(D)

print()

print("Search 기능")
A.Search(2)
A.Search(38)
B.Search(8)
B.Search(-24)

print()

print("IsEmpty 기능")
print("집합 C와 D의 차집합의 공집합 여부 :", E.IsEmpty())

print()

print("Preorder_Traverse 기능")
Preorder_Traverse(A)
Preorder_Traverse(C)

print()

print("Level_Sum 기능")
Level_Sum(C, 3)

print()

print("Inorder nth 기능")
Inorder_nth(C, 5)
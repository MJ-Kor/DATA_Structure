import Binary_Tree as BT
import Searching_Tree as BST

def In_order(n):
    if n is not None:
        In_order(n.left)
        print(n.key, end = ' ')
        In_order(n.right)

class BSTMap():
    def __init__(self):
        self.root = None

    def IsEmpty(self):
        return self.root == None

    def Clear(self):
        self.root = None

    def Size(self):
        return BT.Count_node(self.root)

    def Search(self, key):
        return BST.search_bst(self.root, key)

    def SearchValue(self, value):
        return BST.search_value_bst(self.root, value)

    def FindMax(self):
        return BST.search_max_bst(self.root)

    def FindMin(self):
        return BST.search_min_bst(self.root)

    def Insert(self, key, value = None):
        n = BST.BSTNode(key, value)
        if self.IsEmpty():
            self.root = n
        else:
            BST.insert_bst(self.root, n)

    def Delete(self, key):
        self.root = BST.delete_bst(self.root, key)

    def Display(self, msg = 'BSTMap :'):
        print(msg, end = '')
        In_order(self.root)
        print()


if __name__ == '__main__':
    map = BSTMap()
    data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
    print("[삽입 연산] :",data)
    for key in data:
        map.Insert(key)
    map.Display("[중위 순회] :")

    if map.Search(26) != None:
        print("[탐색 26] : 성공")
    else:
        print("[탐색 26] : 실패")

    if map.Search(25) != None:
        print("[탐색 25] : 성공")
    else:
        print("[탐색 25] : 실패")

    map.Delete(3)
    map.Display("[삭제 3] :")
    map.Delete(68)
    map.Display("[삭제 68] :")
    map.Delete(18)
    map.Display("[삭제 18] :")
    map.Delete(35)
    map.Display("[삭제 35] :")

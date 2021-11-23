from Map_By_BST import *
from AVL_Tree import *
from Searching_Tree import *
from Binary_Tree import *

class AVLMap(BSTMap):
    def __init__(self):
        super().__init__()

    def Insert(self, key, value = None):
        n = BSTNode(key, value)
        if self.IsEmpty():
            self.root = n
        else:
            self.root = Insert_Avl(self.root, n)

    def Display(self, msg = 'AVLMap :'):
        print(msg, end = ' ')
        Level_order(self.root)
        print()

node = [1, 2, 3, 4, 5, 6, 7, 8, 9]
map = AVLMap()
for i in node:
    map.Insert(i)
    map.Display("AVL(%d) :"%i)

print("노드의 개수 = %d" %Count_node(map.root))
print("단말의 개수 = %d" %Count_leaf(map.root))
print("트리의 높이 = %d" %Calc_height(map.root))
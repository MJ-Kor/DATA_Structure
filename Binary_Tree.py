import CircleQueue_By_Python as CQ

class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def Pre_order(n):
    if n is not None:
        print(n.data, end = '')
        Pre_order(n.left)
        Pre_order(n.right)

def In_order(n):
    if n is not None:
        In_order(n.left)
        print(n.data, end = '')
        In_order(n.right)

def Post_order(n):
    if n is not None:
        Post_order(n.left)
        Post_order(n.right)
        print(n.data, end = '')

def Level_order(root):
    queue = CQ.Circle_Queue()
    queue.enQueue(root)
    while not queue.isEmpty():
        n = queue.deQueue()
        if n is not None:
            print(n.data, end = '')
            queue.enQueue(n.left)
            queue.enQueue(n.right)

def Count_node(n):
    if n is None:
        return 0
    else:
        return 1 + Count_node(n.left) + Count_node(n.right)

def Count_leaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return Count_leaf(n.left) + Count_leaf(n.right)

def Calc_height(n):
    if n is None:
        return 0
    hleft = Calc_height(n.left)
    hright = Calc_height(n.right)
    if hleft > hright:
        return hleft + 1
    else:
        return hright + 1

d = TNode('D', None, None)
e = TNode('E', None, None)
b = TNode('B', d, e)
f = TNode('F', None, None)
c = TNode('C', f, None)
root = TNode('A', b, c)

print('\n In-Order : ', end = '')
In_order(root)

print('\n Pre-Order : ', end = '')
Pre_order(root)

print('\n Post-Order : ', end = '')
Post_order(root)

print('\n Level-Order : ', end = '')
Level_order(root)

print()

print("노드의 개수 = %d개" % Count_node(root))
print("단말의 개수 = %d개" % Count_leaf(root))
print("트리의 높이 = %d" % Calc_height(root))

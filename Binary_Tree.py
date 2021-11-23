import CircleQueue_By_Python as CQ
import math

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

def Pre_order2(n):
    if n is not None:

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
            print(n.key, end = ' ')      # AVL 트리 때문에 key로 바꿔놓음 단독으로 쓸때는 data로 바꿀것
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

def Is_balanced(root):
    if root == None:
        return 1, 'True'
    hleft, balance = Is_balanced(root.left)
    hright, balance = Is_balanced(root.right)
    if hleft-hright > -2 and hleft - hright < 2 and balance == 'True':
        if hleft > hright:
            return hleft + 1, 'True'
        else:
            return hright + 1, 'True'
    else:
        if hleft > hright:
            return hleft + 1, 'False'
        else:
            return hright + 1, 'False'

def level(root, node):
    sum = 0
    queue = CQ.Circle_Queue()
    queue.enQueue(root)
    while not queue.isEmpty():
        n = queue.deQueue()
        sum += 1
        if n is not None:
            queue.enQueue(n.left)
            queue.enQueue(n.right)
            if n.data == node:
                return int(math.log2(sum)) + 1



def path_length(root):
    length = 0
    queue = CQ.Circle_Queue()
    queue.enQueue(root)
    while not queue.isEmpty():
        n = queue.deQueue()
        if n is not None:
            node_level = level(root, n.data) - 1
            length += node_level
            queue.enQueue(n.left)
            queue.enQueue(n.right)

    return length


if __name__ == '__main__':
    c = TNode('C', None, None)
    d = TNode('D', None, None)
    f = TNode('F', None, None)
    b = TNode('B', c, d)
    e = TNode('E', None, f)
    root = TNode('A', b, e)

    print('In-Order : ', end = '')
    In_order(root)

    print('\nPre-Order : ', end = '')
    Pre_order(root)

    print('\nPost-Order : ', end = '')
    Post_order(root)

    print('\nLevel-Order : ', end = '')
    Level_order(root)

    print()

    print("노드의 개수 = %d개" % Count_node(root))
    print("단말의 개수 = %d개" % Count_leaf(root))
    print("트리의 높이 = %d" % Calc_height(root))
    print("C 노드의 레벨 : %d" % level(root, 'C'))
    print("균형 트리 :", Is_balanced(root)[1])
    print("전체 경로의 길이 : %d" % path_length(root))


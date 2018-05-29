import random

class TreapNode(object):
    def __init__(self, number):
        self.val = number
        self.rank = random.random()
        self.size = 1
        self.left = None
        self.right = None

class TreapTree(object):
    def __init__(self):
        self.root = None

def get_size(tree):
    if tree is not None:
        return tree.size
    return 0

def update_size(tree):
    if tree is not None:
        tree.size = get_size(tree.left) + 1 + get_size(tree.right)

def split(tree, left, right, pos, add=0): 
    if tree is None:
        left = right = None
        return left, right
    cur_pos = add + get_size(tree.left) + 1
    if cur_pos <= pos:
        tree.right, right = split(tree.right, tree.right, right, pos, cur_pos)
        left = tree
    else:
        left, tree.left = split(tree.left, left, tree.left, pos, add)
        right = tree
    update_size(tree)
    return left, right

def merge(tree, left, right):
    if left is None:
        tree = right
    elif right is None:
        tree = left
    elif left.rank > right.rank:
        left.right = merge(left.right, left.right, right)
        tree = left
    else:
        right.left = merge(right.left, left, right.left)
        tree = right
    update_size(tree)
    return tree

def insert(tree, x, i):
    left = None
    right = None
    xNode = TreapNode(x)
    left, right = split(tree, left, right, i-1)
    left = merge(left, left, xNode)
    tree = merge(tree, left, right)
    return tree

def print_tree(tree):
    if tree is not None:
        print_tree(tree.left)
        print(tree.val)
        print('I have size of ', str(tree.size))
        print_tree(tree.right)

def query2(root, l, r):
    temp1 = temp2 = temp3 = temp4 = None
    temp1, temp2 = split(root, temp1, temp2, r)
    temp3, temp4 = split(temp1, temp3, temp4, l-1)
    temp3 = merge(temp3, temp3, temp2)
    temp3 = merge(temp3, temp3, temp4)
    root = temp3
    return root

def query1(root, l, r):
    temp1 = temp2 = temp3 = temp4 = None
    temp1, temp2 = split(root, temp1, temp2, r)
    temp3, temp4 = split(temp1, temp3, temp4, l-1)
    temp3 = merge(temp3, temp3, temp2)
    temp3 = merge(temp3, temp4, temp3)
    root = temp3
    return root

tree = TreapTree()
if tree.root is None:
    print('WTF, it\'s still empty...')
for i in range(8):
    tree.root = insert(tree.root, i+1, i+1)
print('The root is ' + str(tree.root.val))
print('the tree has size of ' + str(tree.root.size))
print_tree(tree.root)
query1(tree.root, 2, 4)
query2(tree.root, 3, 5)
print_tree(tree.root)









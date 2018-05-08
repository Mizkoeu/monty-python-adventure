import random
import sys

list = []

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

def split(tree, pos, add=0): 
    if tree is None:
        left = right = None
        return left, right
    cur_pos = add + get_size(tree.left) + 1
    if cur_pos <= pos:
        tree.right, right = split(tree.right, pos, cur_pos)
        left = tree
    else:
        left, tree.left = split(tree.left, pos, add)
        right = tree
    update_size(tree)
    return left, right

def merge(left, right):
    if left is None:
        tree = right
    elif right is None:
        tree = left
    elif left.rank > right.rank:
        left.right = merge(left.right, right)
        tree = left
    else:
        right.left = merge(left, right.left)
        tree = right
    update_size(tree)
    return tree

def insert_(tree, x, i):
    left = None
    right = None
    xNode = TreapNode(x)
    left, right = split(tree, i)
    left = merge(left, xNode)
    tree = merge(left, right)
    return tree

def insert(tree, x):
    tree = merge(tree, TreapNode(x))
    return tree

def tree_to_list(tree):
    if tree is not None:
        tree_to_list(tree.left)
        list.append(tree)
        tree_to_list(tree.right)

def query2(root, l, r):
    temp1 = temp2 = temp3 = temp4 = None
    temp1, temp2 = split(root, r)
    temp3, temp4 = split(temp1, l-1)
    temp3 = merge(temp3, temp2)
    root = merge(temp3, temp4)

def query1(root, l, r):
    temp1 = temp2 = temp3 = temp4 = None
    temp1, temp2 = split(root, r)
    temp3, temp4 = split(temp1, l-1)
    temp3 = merge(temp3, temp2)
    root = merge(temp4, temp3)

tree = TreapTree()
initial_input = input().strip().split()
arr_len = int(initial_input[0])
query_count = int(initial_input[1])

arr = input().strip().split()
for i in range(arr_len):
    tree.root = insert(tree.root, int(arr[i]))

for j in range(query_count):
    query = input().strip().split()
    query_type = int(query[0])
    if query_type == 1:
        query1(tree.root, int(query[1]), int(query[2]))
    elif query_type == 2:
        query2(tree.root, int(query[1]), int(query[2]))
    else:
        exit

tree_to_list(tree.root)
out = abs(list[0].val - list[arr_len-1].val)
print(str(out))
for node in list:
    print(node.val, end=" ")

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self) -> str:
        return str(self.val)
A=[1]
B=[2]
C=[3]
A.left=A
B.left=B
C.left=C
print(A)

A1 =TreeNode(1)
A2=TreeNode(2)
B1=TreeNode(3)
B2= TreeNode(8)
C1=TreeNode(1)
C2= TreeNode(-1)
A2.left,A2.right =B2 , C2
print(A2)

def pre_order(node):
    if not node:
        return
    print(node)
    pre_order(node.left)
    pre_order(node.right)
pre_order(A)

def in_order(node):
    if not node:
        return
    print(node)
    pre_order(node.left)
    print(node)
    pre_order(node.right)
pre_order(A)

def pre_order_iterative(node):
    stk=[node]
    while stk:
        node = stk.pop()
        print(node)
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)
pre_order_iterative(A)
from collections import deque

def level_order(node):
    q= deque()
    q.append(node)
    
    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
level_order(A)

def search(node,target):
    if not node:
        return False
    if node.val == target:
        return True
    return search(node.left, target) or search(node.right, target)
search(A,6)

def search_bst(node,target):
    if not node:
        return False
    
    if node.val == target:
        return True
    
    if target < node.val: return search_bst(node.left,target)
    else: return search_bst(node.right,target)
search_bst(A2,4)
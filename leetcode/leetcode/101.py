# Definition for a binary tree node.
<<<<<<< Tabnine <<<<<<<
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
>>>>>>> Tabnine >>>>>>>

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(t1: TreeNode, t2: TreeNode) -> bool:
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)
        
        return isMirror(root, root)

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        q = deque([(root.left, root.right)])
        
        while q:
            t1, t2 = q.popleft()
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            q.append((t1.left, t2.right))
            q.append((t1.right, t2.left))
        
        return True
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        stack = [(root.left, root.right)]
        
        while stack:
            t1, t2 = stack.pop()
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            stack.append((t1.left, t2.right))
            stack.append((t1.right, t2.left))
        
        return True


            
                
                
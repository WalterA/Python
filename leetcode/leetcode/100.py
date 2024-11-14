# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

#davide
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def preOrder_iterative(root) -> list:
            result: list = []  # Initialize an empty list to store the pre-order traversal
            stack: list = [root]  # Initialize the stack with the root node

            while stack:
                node = stack.pop()  # Pop a node from the stack

                if node:
                    result.append(node.val)  # If the node is not None, append its value to the result list
                    stack.append(node.right)  # Push the right child onto the stack
                    stack.append(node.left)   # Push the left child onto the stack
                else:
                    result.append("null")  # If the node is None, append "null" to the result list

            return result  # Return the list representing the pre-order traversal of the tree

        # Compare the pre-order traversals of both trees
        return preOrder_iterative(p) == preOrder_iterative(q)

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        queue = deque([(p, q)])
        
        while queue:
            node1, node2 = queue.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
        
        return True

p = [1,2,3]
q = [1,2,3]
# Creazione degli alberi p e q
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

# Creazione dell'oggetto Solution e chiamata del metodo isSameTree
sol = Solution()
result = sol.isSameTree(p, q)

# Stampa del risultato
print("Gli alberi p e q sono uguali?", result)


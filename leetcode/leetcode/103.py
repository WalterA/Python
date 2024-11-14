# Definizione del nodo dell'albero binario
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Creazione dell'albero binario
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Classe Solution con il metodo zigzagLevelOrder
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        
        lista = []
        q = deque([root])
        left_to_right = True
        
        while q:
            level_size = len(q)
            level_nodes = []
            
            for _ in range(level_size):
                node = q.popleft()
                level_nodes.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if not left_to_right:
                level_nodes.reverse()
            
            lista.append(level_nodes)
            left_to_right = not left_to_right
        
        return lista

# Esecuzione del test
sol = Solution()
result = sol.zigzagLevelOrder(root)
print("Lista dei nodi in ordine zigzag:", result)

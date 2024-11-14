from collections import deque


# Definizione del nodo dell'albero binario
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Classe Solution con il metodo levelOrder
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        
        lista = []
        q = deque([root])
        
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
            
            lista.append(level_nodes)
        
        return lista

# Creazione dell'albero binario
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Esecuzione del test
sol = Solution()
result = sol.levelOrder(root)
print("Lista dei nodi in ordine di livello:", result)







import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        lista=[]
        if not root:
            return []
        left= self.binaryTreePaths(root.left)
        right= self.binaryTreePaths(root.right)
        if not left and not right:
            lista.append(str(root.val))
        for path in left + right:
            lista.append(str(root.val) + '->' + path)
        return lista

class TestBinaryTreePaths(unittest.TestCase):
    def test_binary_tree_paths(self):
        # Crea l'albero binario [1, 2, 3, None, 5]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)

        sol = Solution()
        result = sol.binaryTreePaths(root)
        expected = ["1->2->5", "1->3"]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
        
        
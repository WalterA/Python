# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# from typing import Optional


# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if root == None:
#             return 0

#         left_depth = self.maxDepth(root.left)
#         right_depth = self.maxDepth(root.right)
#         return 1 + max(left_depth, right_depth)

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        leftSubHeight = self.maxDepth(root.left)
        rightSubHeight = self.maxDepth(root.right)

        return max(leftSubHeight, rightSubHeight) + 1
def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while i < len(nodes):
        current = queue.pop(0)
        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    return root

# Test case
root = build_tree([3, 9, 20, None, None, 15, 7])
solution = Solution()
print(solution.maxDepth(root)) 


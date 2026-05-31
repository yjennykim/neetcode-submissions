# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def recurse(node):
            if not node:
                return 0

            leftDepth = recurse(node.left)
            rightDepth = recurse(node.right)

            return max(leftDepth, rightDepth) + 1
        
        return recurse(root)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def recurse(node):
            if not node:
                return 0, True

            leftHeight, isLeftBalanced = recurse(node.left)
            if not isLeftBalanced:
                return -1, False

            rightHeight, isRightBalanced = recurse(node.right)
            if not isRightBalanced:
                return -1, False

            return max(leftHeight, rightHeight) + 1, abs(leftHeight - rightHeight) <= 1
        
        height, isBalanced = recurse(root)
        return isBalanced
        

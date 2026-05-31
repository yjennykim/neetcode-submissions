# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def recurse(node):
            if not node:
                return 
            
            left = recurse(node.left)
            right = recurse(node.right)
            
            tempLeft = node.left
            node.left = node.right
            node.right = tempLeft

            return node

        return recurse(root)
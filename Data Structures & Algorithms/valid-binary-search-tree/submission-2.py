# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def is_valid(node,l,r):
            if not node: 
                return True
            
            if l < node.val < r:
                return is_valid(node.left, l, node.val) and is_valid(node.right, node.val, r)
            
            return False
        
        return is_valid(root, -math.inf, math.inf)
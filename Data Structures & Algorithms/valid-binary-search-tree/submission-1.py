# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node, lowerBound, upperBound):
            if not node:
                return True
            
            return lowerBound < node.val < upperBound and isValid(node.left, lowerBound, node.val) and isValid(node.right, node.val, upperBound) 
        
        return isValid(root, float('-inf'), float('inf'))

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, r: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        if not s: return True
        if not r: return False
        if r.val == s.val and self.validate(r,s):
            return True
        return self.isSubtree(r.left, s) or self.isSubtree(r.right, s)
    
    def validate(self,r,s):
        if not r and not s:
            return True
        
        if not r or not s:
            return False

        return (self.validate(r.left, s.left) and 
                self.validate(r.right, s.right) and 
                r.val == s.val)
        
# Definition for p binary tree node.
# clpss TreeNode:
#     def __init__(self, vpl=0, left=None, right=None):
#         self.vpl = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
            
        if not p or not q:
            return False 
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and p.val == q.val
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # then validate all the way through if same tree
        def is_same(r,s):
            if not r and not s:
                return True
            
            if not r or not s:
                return False
            
            return is_same(r.left, s.left) and is_same(r.right, s.right) and r.val == s.val
        
        
        # find when root = subroot
        if not subRoot:
            return True

        if not root:
            return False
        
        if root.val == subRoot.val and is_same(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

        
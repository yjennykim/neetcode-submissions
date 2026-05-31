# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # Helper function to check if two trees are identical
        def isSameTree(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            return (s.val == t.val) and isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

        # Base case: if subRoot is None, it's always a subtree
        if not subRoot:
            return True
        # If root is None, then subRoot can't be a subtree
        if not root:
            return False
        
        # Check if current tree rooted at root is the same as subRoot
        if isSameTree(root, subRoot):
            return True
        
        # Recursively check left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = [0]

        def recurse(node):
            if not node: 
                return None
            
            c = recurse(node.left)
            if c: return c

            n[0] += 1
            print("n=", n, "node=", node.val)
            if n[0] == k: 
                return node.val
            
            c = recurse(node.right)
            if c: return c

            return None
        
        return recurse(root)
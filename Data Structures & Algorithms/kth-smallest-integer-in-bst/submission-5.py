# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.save = None
        self.count = k

        def dfs(node):
            if self.save: 
                return
            if not node:
                return
            
            dfs(node.left)
            self.count -= 1
            if self.count == 0:
                self.save = node
                return

            dfs(node.right)

        dfs(root)
        return self.save.val
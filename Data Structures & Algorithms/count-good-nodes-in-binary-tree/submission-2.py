# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0

        def dfs(node, max_num):
            if not node:
                return
            
            if node.val >= max_num:
                self.good += 1
            
            dfs(node.left, max(max_num, node.val))
            dfs(node.right, max(max_num, node.val))
        
        dfs(root, -math.inf)
        return self.good
            

                
            
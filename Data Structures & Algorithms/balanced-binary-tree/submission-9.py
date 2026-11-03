# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return True, 0 

            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)
            curr_height = max(left_height, right_height) + 1

            if not left_balanced or not right_balanced:
                return False, curr_height
            
            return abs(left_height - right_height) <= 1, curr_height
        
        is_bal, _ = dfs(root)
        return is_bal
        
        
            

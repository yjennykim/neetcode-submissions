# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # at every level, get the most right 
        levels = {}

        def recurse(node, level):
            if not node:
                return
            
            if level not in levels:
                levels[level] = []
            levels[level].append(node.val)

            recurse(node.left, level+1)
            recurse(node.right, level+1)
        
        recurse(root, 0)
        res = []
        for i, level in enumerate(levels):
            res.append(levels[level][-1])
        
        return res
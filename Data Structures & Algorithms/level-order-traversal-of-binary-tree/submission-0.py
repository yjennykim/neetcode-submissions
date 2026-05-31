# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []

        def recurse(node, level):
            if not node:
                return

            if len(levels) == level:
                levels.append([])
            
            levels[level].append(node.val)
            recurse(node.left, level + 1)
            recurse(node.right, level + 1)

        recurse(root, 0)
        return levels
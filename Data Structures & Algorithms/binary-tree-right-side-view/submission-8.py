# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []
        queue = collections.deque()
        if not root: return levels

        queue.append((root, 0))
        while queue:
            node, level = queue.popleft()
            if len(levels) == level:
                levels.append(node.val)
            
            if node.right:
                queue.append((node.right, level + 1))
            if node.left:
                queue.append((node.left, level + 1))

        return levels

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ordering = []
        if not root:
            return ordering
        q = deque()
        q.append((root, 0))

        while q:
            node, curr_level = q.popleft()
            if curr_level >= len(ordering):
                ordering.append([])
            
            ordering[-1].append(node.val)
            if node.left:
                q.append((node.left, curr_level + 1))
            if node.right:
                q.append((node.right, curr_level + 1))
        
        return ordering            

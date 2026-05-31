# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []

        queue = collections.deque([root])

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if i == 0:
                    res.append(curr.val)
                
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
        return res
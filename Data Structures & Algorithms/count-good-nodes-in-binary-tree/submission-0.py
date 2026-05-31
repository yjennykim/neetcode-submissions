# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        countGoodNodes = [0]

        def recurse(node, maxSeen):
            if not node:
                return
            
            if node.val >= maxSeen:
                countGoodNodes[0] += 1

            recurse(node.left, max(maxSeen, node.val))
            recurse(node.right, max(maxSeen, node.val))
        
        recurse(root, -101)

        return countGoodNodes[0]
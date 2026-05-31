# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recurse(node, res):
            if not node:
                res.append("null")
                return
            
            recurse(node.left, res)
            recurse(node.right, res)
            
            res.append(node.val)
            return node.val
        
        pTree = []
        qTree = []

        recurse(p, pTree)
        recurse(q, qTree)

        print(f"Checking {pTree} {qTree}")
        return qTree == pTree
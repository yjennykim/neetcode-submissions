# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def recurse(node, order):
            if not node:
                order.append("Null")
                return

            order.append(str(node.val))
            recurse(node.left, order)
            recurse(node.right, order)

            

        original = []
        sub = []


        recurse(root, original)
        recurse(subRoot, sub)
        print(f"sub {sub}\noriginal {original}")

        strSub = "".join(sub) 
        strOrig = "".join(original)

        print(f"sub {strSub}\noriginal {strOrig}")
        return strSub in strOrig
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxHeight = [0]

        def recurse(node, maxHeight):
            if not node:
                return 0
            
            leftHeight = recurse(node.left, maxHeight)
            rightHeight = recurse(node.right, maxHeight)

            maxHeight[0] = max(leftHeight + rightHeight  , maxHeight[0])

            return max(leftHeight, rightHeight) + 1
        
        recurse(root, maxHeight)
        return maxHeight[0]
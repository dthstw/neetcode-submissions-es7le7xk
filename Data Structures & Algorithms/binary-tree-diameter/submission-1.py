# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.maxDiam = 0

        def maxDepth(root):
            if not root:
                return 0 
            left = maxDepth(root.left)
            right = maxDepth(root.right)

            self.maxDiam = max(self.maxDiam, left + right)

            return 1 + max(left, right)

        maxDepth(root)

        return self.maxDiam
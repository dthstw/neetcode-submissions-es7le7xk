# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(tr1, tr2):
            if not tr1 and not tr2:
                return True
            
            if tr1 and tr2:
                return tr1.val == tr2.val and sameTree(tr1.left, tr2.left) and sameTree(tr1.right, tr2.right)
            return False

        if not root:
            return False
        
        if root and subRoot:
            return sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


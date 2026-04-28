# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        res = []
        self.q = deque([root])
        while self.q:
            sub_arr = []
            for i in range(len(self.q)):
                curr = self.q.popleft()
                sub_arr.append(curr)
            for _ in sub_arr:
                if _.left:
                    self.q.append(_.left)
                if _.right:
                    self.q.append(_.right)
            res.append([i.val for i in sub_arr])
        
        return res
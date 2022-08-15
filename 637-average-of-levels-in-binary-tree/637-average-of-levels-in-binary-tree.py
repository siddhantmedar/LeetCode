# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        
        q = deque([root])
        
        while q:
            n = len(q)
            sm = 0
            sz=0
            
            for i in range(n):
                node = q.popleft()
                sm+=node.val
                sz+=1
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
            res.append(sm/sz)
            
        return res
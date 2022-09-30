# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        
        q = deque([root])
        
        while q:
            n = len(q)
            num = 0
            den = 0
            
            for k in range(n):
                node = q.popleft()
                
                num+=node.val
                den+=1
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
            result.append(num/den)
            
        return result
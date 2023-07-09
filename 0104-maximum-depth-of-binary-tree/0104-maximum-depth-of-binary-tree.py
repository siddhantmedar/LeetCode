# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def bfs(root):     
            if not root:
                return False
            
            q = deque([(root)])
            
            res = 0
            
            while q:
                n=len(q)
                
                for _ in range(n):
                    node = q.popleft()
                    
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                
                res+=1
                    
            return res
        
        if not root:
            return 0
        
        return bfs(root)
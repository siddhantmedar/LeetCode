# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         def dfs(p,q):
#             if (p and not q) or (not p and  q):
#                 return False
            
#             if not p and not q:
#                 return True
            
#             return p.val==q.val and dfs(p.left,q.left) and dfs(p.right,q.right)

        
        def bfs(p,q):
            if (p and not q) or (not p and q):
                return False
            
            qq = deque([(p,q)])
            
            while qq:
                n = len(qq)
                
                for _ in range(n):
                    p,q = qq.popleft()
                    
                    if (p and not q) or (not p and q) or (p and q and p.val != q.val):
                        return False
                    
                    if p and q:
                        qq.append((p.left,q.left))
                        qq.append((p.right,q.right))
            
            return True
        
        
        return bfs(p,q)
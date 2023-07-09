# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(r1, r2):
            if not r1:
                return r2
            
            if not r2:
                return r1
            
            if not r1 and not r2:
                return r1
            
            q = deque([(r1,r2,None,0)])
            
            root = r1
            
            while q:
                n = len(q)
                
                for _ in range(n):
                    r1,r2,p,left = q.popleft()
                    
                    if not r1 and not r2:
                        continue

                    elif not r1 and r2:
                        if left:
                            p.left = r2
                        else:
                            p.right = r2

                    elif r1 and r2:
                        r1.val+=r2.val

                        q.append((r1.left,r2.left,r1,1))
                        q.append((r1.right,r2.right,r1,0))

            return root
            
        
        return bfs(root1,root2)
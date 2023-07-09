# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def bfs(root):
            q = deque([(root,[])])
            res = []
            
            while q:
                n = len(q)
                
                for _ in range(n):
                    node,path = q.popleft()
                    
                    if not node:
                        continue
                        
                    path.append(str(node.val))

                    if not node.left and not node.right:
                        res.append("->".join(path))
                    
                    if node.left:
                        q.append((node.left,path[::]))
                    if node.right:
                        q.append((node.right,path[::]))

            return res
        
        
        # def dfs(root):
#             nonlocal res, path
            
#             if not root:
#                 return 
            
#             path.append(str(root.val))
            
#             if not root.left and not root.right:
#                 res.append("->".join(path))
#                 path.pop()
#                 return
            
#             dfs(root.left)
#             dfs(root.right)
            
#             path.pop()
        
        
        # res = []
        # path = []
        
        return bfs(root)
        
        # return res
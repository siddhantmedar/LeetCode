# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
       
        
        def bfs(root):
            res = 0
            
            if not root:
                return res
            
            q = deque([(root,1)])
                
            while q:
                n = len(q)
                
                node,level = q.popleft()

                if not node.left and not node.right:
                    res = level
                    break

                if node.left:
                    q.append((node.left, level+1))

                if node.right:
                    q.append((node.right, level+1))
            
            return res
        
        
        return bfs(root)
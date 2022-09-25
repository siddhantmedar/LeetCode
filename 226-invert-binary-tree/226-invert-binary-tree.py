# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(root):
            if not root:
                return
            
            q = deque([root])

            while q:
                n = len(q)
                
                for k in range(n):
                    node = q.popleft()
                    
                    node.left, node.right = node.right, node.left
                    
                    if node.left:
                        q.append(node.left)
                        
                    if node.right:
                        q.append(node.right)
        
        bfs(root)
        
        return root
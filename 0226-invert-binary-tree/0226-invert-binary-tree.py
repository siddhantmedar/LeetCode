# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def solve(root):
            if not root:
                return 
            
            root.left, root.right = root.right, root.left
            
            solve(root.left)
            solve(root.right)
            
            return root
            
        # return solve(root)
    
    
        def solve2(root):
            if not root:
                return root
            
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
                        
            return root
        
        return solve2(root)
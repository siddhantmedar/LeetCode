# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        
        while q:
            n = len(q)
            tmp = []
            for k in range(n):
                node = q.popleft()
                tmp.append(node)
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
        
        
        def dfs(root):
            if not root:
                return root
            
            if root in tmp:
                return root
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left and right:
                return root
            
            return left or right
        
        return dfs(root)
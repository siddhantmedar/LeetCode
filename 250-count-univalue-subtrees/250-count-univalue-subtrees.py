# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def same(root, x):
            if not root:
                return True
            
            return root.val == x and same(root.left, x) and same(root.right, x)
        
        
        def dfs(root):
            nonlocal result
            
            if not root:
                return
            
            if same(root, root.val):
                result+=1
                
            dfs(root.left)
            dfs(root.right)
            
        
        result = 0
        
        dfs(root)
        
        return result
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal count
            
            if not root:
                return True
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if not left or not right:
                return False
            
            if (root.left and root.val != root.left.val)\
            or (root.right and root.val != root.right.val):
                return False
            
            count+=1
            return True
        
        
        count = 0
        
        dfs(root)
        
        return count
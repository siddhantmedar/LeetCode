# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def solve(root, target):
            nonlocal count
            
            if not root:
                return
            
            if root.val-target == 0:
                count+=1
                
            solve(root.left, target-root.val)
            solve(root.right, target-root.val)
            
        
        def dfs(root):
            if not root:
                return
            
            solve(root, targetSum)
            
            dfs(root.left)
            dfs(root.right)
            
            
        count = 0
        
        dfs(root)
        
        return count
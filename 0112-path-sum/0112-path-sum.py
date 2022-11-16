# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        def dfs(root, rem):
            if not root:
                return False
            
            if (not root.left and not root.right) and root.val-rem == 0:
                return True
            
            return dfs(root.left,rem-root.val) or dfs(root.right, rem-root.val)
        
        
        return dfs(root, target)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return (0, True)
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            nb = False
            if abs(left[0]-right[0]) > 1 or not left[1] or not right[1]:
                nb = True
                
            return (max(left[0],right[0])+1, True if not nb else False)
        
        return dfs(root)[1]
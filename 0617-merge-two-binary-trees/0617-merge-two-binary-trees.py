# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(r1, r2):
            if not r1 and not r2:
                return r1
            
            elif not r1 and r2:
                return r2
            
            elif r1 and not r2:
                return r1
            
            else:
                r1.val+=r2.val
                
                r1.left = dfs(r1.left,r2.left)
                r1.right = dfs(r1.right,r2.right)
                
                return r1
            
        return dfs(root1,root2)
            
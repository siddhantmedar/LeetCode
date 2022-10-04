# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root):
            nonlocal path, result
            
            if not root:
                return
            
            path.append(root.val)
            
            if not root.left and not root.right and sum(path) == targetSum:
                result.append(path[:])
                path.pop()
                return
                
                
            dfs(root.left)
            dfs(root.right)
            
            path.pop()
            
        
        path, result = [], []
        
        dfs(root)
        
        return result
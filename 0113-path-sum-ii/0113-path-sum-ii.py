# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        def dfs(root, rem):
            nonlocal path, result
            
            if not root:
                return False
            
            path.append(root.val)
            
            if not root.left and not root.right:
                if root.val-rem == 0:
                    result.append(path[:])
                    
                path.pop()
                return
            
            left = dfs(root.left, rem-root.val)
            right = dfs(root.right, rem-root.val)
            
            if not left and not right:
                path.pop()
                
            return False
        
        result = []
        path = []
        
        dfs(root, target)
        
        return result
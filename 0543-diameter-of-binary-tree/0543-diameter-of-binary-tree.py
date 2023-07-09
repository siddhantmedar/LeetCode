# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        
        def dfs(root):
            if not root:
                return 0,0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            up = max(left[0],right[0])+1
            node = max(left[1], right[1], left[0]+right[0])
            
            return (up,node)
        
        return dfs(root)[1]
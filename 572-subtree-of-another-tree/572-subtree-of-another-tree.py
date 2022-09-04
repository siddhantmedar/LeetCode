# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def isSame(root1, root2):
            if not root1 and not root2:
                return True
            
            elif (not root1 and root2) or (not root2 and root1):
                return False
            
            return root1.val == root2.val and isSame(root1.left, root2.left) and isSame(root1.right, root2.right)
            
        def dfs(root):
            if not root:
                return
            
            if isSame(root, root2):
                return True
            
            return dfs(root.left) or dfs(root.right)
        
        return dfs(root1)
    
        
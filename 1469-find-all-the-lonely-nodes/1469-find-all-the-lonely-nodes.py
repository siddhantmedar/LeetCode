# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if not root:
                return []
            
            lst = []
            
            if (not root.left and root.right) or (root.left and not root.right):
                lst.append(root.left.val if root.left else root.right.val)
                
            return lst+dfs(root.left)+dfs(root.right)
        
        
        return dfs(root)
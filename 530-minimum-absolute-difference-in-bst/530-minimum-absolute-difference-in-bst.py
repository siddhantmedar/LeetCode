# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(root):
            return inorder(root.left)+[root.val]+inorder(root.right) if root else []
        
        lst = inorder(root)
        res = float("inf")
        
        for i in range(len(lst)-1):
            res = min(res, lst[i+1]-lst[i])
            
        return res
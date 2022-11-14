# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root, mn, mx):
            if not root:
                return True
            
            if not mn<root.val<mx:
                return False
            
            return check(root.left,mn, root.val) and check(root.right, root.val, mx)
            
        return check(root, float("-inf"), float("inf"))
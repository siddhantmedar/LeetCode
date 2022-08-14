# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def solve(root, pre=float("-inf")):
            nonlocal count

            if not root:
                return
            
            if root.val >= pre:
                count+=1
                
            solve(root.left, max(pre, root.val))
            solve(root.right, max(pre, root.val))
            
        
        count = 0
        
        solve(root)
        
        return count
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if not root:
                return float("inf")

            if not root.left and not root.right:
                return 1

            left = solve(root.left)
            right = solve(root.right)

            return min(left, right)+1
            
        result = solve(root)
        
        return result if result != float("inf") else 0
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def solve(s,e):
            if s > e:
                return None
            
            mid = (s+e)>>1
            
            root = TreeNode(nums[mid])
            
            root.left = solve(s, mid-1)
            
            root.right = solve(mid+1, e)
            
            return root
        
        return solve(0, len(nums)-1)
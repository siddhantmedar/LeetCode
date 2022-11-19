# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def solve(low, high):
            if low > high:
                return None
            
            if low == high:
                return TreeNode(nums[low])
            
            mid = (low+high)>>1
            root = TreeNode(nums[mid])
            
            root.left = solve(low,mid-1)
            root.right = solve(mid+1,high)
            
            return root
        
        
        return solve(0,len(nums)-1)
        
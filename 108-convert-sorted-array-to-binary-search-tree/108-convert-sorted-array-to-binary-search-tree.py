# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def solve(start, end):
            if start == end:
                return TreeNode(nums[start])
            
            if start < end:
                mid = (start+end)>>1
                
                root = TreeNode(nums[mid])
                
                root.left = solve(start,mid-1)
                root.right = solve(mid+1, end)
                
                return root
            
            else:
                return None
            
            
        return solve(0, len(nums)-1)
        
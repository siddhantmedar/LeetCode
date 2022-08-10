# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def util(self, nums: List[int], start, end)->TreeNode:
        if start > end:
            return None
        mid = (start+end)//2
        root = TreeNode(nums[mid])
        root.left = self.util(nums,start, mid-1)
        root.right = self.util(nums, mid+1, end)
        return root
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        return self.util(nums, 0, len(nums)-1)
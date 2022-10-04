# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def getMax(l,r):
            result = float("-inf")
            idx = None
            
            for i in range(l, r+1):
                if nums[i] > result:
                    result = nums[i]
                    idx = i
                    
            return idx 
        
        
        def solve(l,r):
            if l > r:
                return None
            
            elif l == r:
                return TreeNode(nums[l])
            
            elif l < r:
                mxIdx = getMax(l,r)

                root = TreeNode(nums[mxIdx])

                root.left = solve(l, mxIdx-1)

                root.right = solve(mxIdx+1,r)

                return root
            
            
        return solve(0, len(nums)-1)
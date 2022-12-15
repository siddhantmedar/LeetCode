class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx, res = nums[0], nums[0]
        
        for ele in nums[1:]:
            mx = max(ele,mx+ele)
            res = max(res,mx)
            
        return res

#     -2 1 -3 4 -1 2 1 -5 4
#                         _
        
#     -2
#     1
#     -2
#     4
#     3
#     5
#     6
#     1
#     5
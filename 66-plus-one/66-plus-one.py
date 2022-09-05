class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        carry = 1
        
        for i in range(len(nums)-1,-1,-1):
            sm = nums[i] + carry
            
            nums[i] = sm%10
            carry = sm//10
            
        if carry:
            return [carry]+nums
        
        return nums
            
#             9 9 9
#             1 1 1
#           1 0 0 0
                
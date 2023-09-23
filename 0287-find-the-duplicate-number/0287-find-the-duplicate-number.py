class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i,ele in enumerate(nums):
            idx = abs(ele)-1
            
            if nums[idx] < 0:
                return abs(ele)
            
            else:
                nums[idx] = -nums[idx]
            
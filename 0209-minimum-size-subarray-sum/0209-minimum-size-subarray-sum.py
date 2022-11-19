class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float("inf")
        sm = 0
        
        i = 0
        for j,ele in enumerate(nums):
            if sm < target:
                sm+=ele
               
            while sm >= target:
                result = min(result,j-i+1)
                sm-=nums[i]
                i+=1

        return result if result != float("inf") else 0
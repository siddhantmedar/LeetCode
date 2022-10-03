class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sm = 0
        
        result = float("inf")
        
        i = 0
        
        for j,ele in enumerate(nums):
            if sm < target:
                sm+=nums[j]
                
            if sm >= target:
                while sm>=target:
                    result = min(result, j-i+1)
                    sm-=nums[i]
                    i+=1
                        
        if sm == target:
            result = min(result, len(nums)-i)
            
        return result if result!=float("inf") else 0
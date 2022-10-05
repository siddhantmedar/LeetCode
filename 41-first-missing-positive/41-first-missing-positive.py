class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i,ele in enumerate(nums):
            if ele < 0:
                nums[i] = 0
                
        for i,ele in enumerate(nums):
            x = abs(ele)
            if 1<=x<=len(nums):
                idx = x-1
                
                if nums[idx] > 0:
                    nums[idx]*=-1
                    
                elif nums[idx] == 0:
                    nums[idx] = -1*(len(nums)+10)
                    
        for i in range(1,len(nums)+1):
            if nums[i-1] >= 0:
                return i
            
        return len(nums)+1
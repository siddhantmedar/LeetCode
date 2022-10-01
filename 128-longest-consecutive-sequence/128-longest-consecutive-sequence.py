class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        
        result = 0
        count = 1
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
                
            if nums[i]+1 == nums[i+1]:
                count+=1
                
            else:
                result = max(result, count)
                count = 1
                
        result = max(result, count)
        
        return result if nums else 0
    
    # [0,0,1,2,3,4,5,6,7,8]
    
    [0,1,1,2]
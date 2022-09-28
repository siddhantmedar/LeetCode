class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = []
        
        for i, ele in enumerate(nums):
            if i>0 and nums[i] == nums[i-1]:
                    continue
            
            l, r = i+1, len(nums)-1
            
            while l < r:
                sm = nums[i]+nums[l]+nums[r]
                
                if sm > 0:
                    r-=1
                    
                elif sm < 0:
                    l+=1
                    
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    l+=1
                    
                    while l<r and nums[l-1] == nums[l]:
                        l+=1
                        
        return result
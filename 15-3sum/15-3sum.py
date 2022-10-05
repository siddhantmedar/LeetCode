class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = []
        
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
                
            left, right = i+1, len(nums)-1
            
            while left < right:
                sm = nums[i] + nums[left] + nums[right]
                
                if sm > 0:
                    right-=1
                    
                elif sm < 0:
                    left+=1
                    
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left+=1
                    
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
        
        return result
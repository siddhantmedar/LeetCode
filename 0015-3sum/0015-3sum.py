class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = []
        
        for i in range(len(nums)-2):
            if i-1>=0 and nums[i-1] == nums[i]:
                continue
                
            low, high = i+1, len(nums)-1
            
            while low < high:
                sm = nums[i]+nums[low]+nums[high]
                
                if sm == 0:
                    result.append([nums[i],nums[low],nums[high]])
                    
                    low+=1
                    
                    while low-1>=0 and low < len(nums) and nums[low-1] == nums[low]:
                        low+=1
                    
                elif sm > 0:
                    high-=1
                    
                else:
                    low+=1
            
        return result
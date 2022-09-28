class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        diff = float("inf")
        
        for i in range(len(nums)):
            l,r = i+1, len(nums)-1
            
            while l < r:
                sm = nums[i]+nums[l]+nums[r]
                
                if abs(target-sm) < abs(diff):
                    diff = target-sm
                    
                if sm < target:
                    l+=1
                    
                else:
                    r-=1
            
            if diff == 0:
                break
                
        return target-diff
    
        # [-4,-1,1,2]
        
        
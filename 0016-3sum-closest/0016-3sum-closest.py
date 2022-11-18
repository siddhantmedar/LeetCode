class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        diff = float("inf")
        
        for i in range(len(nums)):
            left, right = i+1, len(nums)-1
            
            while left < right:
                sm = nums[i]+nums[left]+nums[right]
                
                if abs(target-sm) < abs(diff):
                    diff = target-sm
                
                if sm < target:
                    left+=1
                        
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                else:
                    right-=1
                
            if diff == 0:
                break
            
            
        return target-diff


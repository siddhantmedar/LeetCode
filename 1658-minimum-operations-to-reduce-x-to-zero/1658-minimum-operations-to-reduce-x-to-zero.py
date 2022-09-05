class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if sum(nums) < x:
            return -1
        
        elif sum(nums) == x:
            return len(nums)
        
        target = sum(nums) - x
        
        mx = float("-inf")
        
        sm = 0
        
        i = 0
        
        for j in range(len(nums)):
            if sm < target:
                sm+=nums[j]
                
            if sm >= target:
                while sm>=target:
                    if sm == target:
                        if j-i+1 > mx:
                            mx = j-i+1
                    
                    sm-=nums[i]
                    i+=1
        
        if sm == target:
            mx = max(mx, len(nums)-i)
        
        return len(nums)-mx if mx != float("-inf") else -1
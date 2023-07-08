class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p1, p2 = 0, len(nums)-1
        
        while p1<len(nums) and p2 >= 0 and p1 < p2:
            sm = nums[p1]+nums[p2]
            
            if sm == target:
                return[p1+1, p2+1]
            
            if sm > target:
                p2-=1
                
            if sm < target:
                p1+=1
                    
            
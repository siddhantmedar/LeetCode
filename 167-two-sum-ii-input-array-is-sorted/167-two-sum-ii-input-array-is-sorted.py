class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums)-1
        
        while low < high:
            sm = nums[low]+nums[high]
            
            if sm == target:
                return [low+1, high+1]
            
            if sm > target:
                high-=1
                
            else:
                low+=1
class Solution:
    def nextGreatestLetter(self, nums: List[str], target: str) -> str:
        s,e = 0, len(nums)-1
        res = None
        
        while s<=e:
            mid = e+(s-e)//2
            
            if nums[mid] > target:
                res = nums[mid]
                e = mid-1
                
            else:
                s=mid+1
                
        return nums[0] if not res else res
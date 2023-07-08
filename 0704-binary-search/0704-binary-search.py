class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def solve(s,e):
            if s > e:
                return -1
            
            mid = e+(s-e)//2
            
            if nums[mid]==target:
                return mid
            
            elif nums[mid] > target:
                return solve(s,mid-1)
                
            else:
                return solve(mid+1,e)
        
        return solve(0, len(nums)-1)
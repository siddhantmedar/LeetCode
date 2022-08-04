class Solution:
    def findFinalValue(self, nums: List[int], n: int) -> int:
        st = set(nums)
        
        while n in nums:
            n*=2
        
        return n
            
        
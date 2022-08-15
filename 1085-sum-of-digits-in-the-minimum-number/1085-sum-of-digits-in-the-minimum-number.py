class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        mn = float("inf")
        
        for ele in nums:
            mn = min(mn, ele)
            
        res = 0
        
        while mn:
            res+=(mn%10)
            mn//=10
            
        return 0 if res%2 else 1
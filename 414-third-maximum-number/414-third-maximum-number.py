class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first, second, third = float("-inf"), float("-inf"), float("-inf")
        
        for ele in set(nums):
            if ele > first:
                third = second
                second = first
                first = ele
                
            elif ele > second:
                third = second
                second = ele
                
            elif ele > third:
                third = ele
                
        return third if third!=float("-inf") else first
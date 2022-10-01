class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        left, right = [0]*n, [0]*n
        
        left[0], right[n-1] = 1,1
        
        for i in range(1, n):
            left[i] = left[i-1]*nums[i-1]
            
        for i in range(n-2, -1, -1):
            right[i] = right[i+1]*nums[i+1]
        
        result = []
        
        for i in range(n):
            result.append(left[i]*right[i])
            
        return result
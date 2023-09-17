class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l,r = [0]*n, [0]*n
        
        l[0] = 1
        r[n-1] = 1
        
        for i in range(1,n):
            l[i] = l[i-1]*nums[i-1]
            
        for i in range(n-2,-1,-1):
            r[i] = r[i+1]*nums[i+1]
            
        return [a*b for a,b in zip(l,r)]
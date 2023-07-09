class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]
        
        left[0] = nums[0]
        right[n-1] = nums[n-1]
        
        for i in range(1,n):
            left[i] = left[i-1]*nums[i]
            
        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1]*nums[i]
            
        print(left, right)
        
        res = []
        
        for i in range(len(nums)):
            if i==0:
                res.append(right[i+1])
                
            elif i==n-1:
                res.append(left[i-1])
                
            else:
                res.append(left[i-1]*right[i+1])
                
        return res
            
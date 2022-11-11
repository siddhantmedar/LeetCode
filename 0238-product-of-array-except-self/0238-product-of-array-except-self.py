class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [0]*len(nums), [0]*len(nums)
        
        left[0] = 1
        right[len(nums)-1] = 1
        
        for i in range(1, len(left)):
            left[i] = left[i-1]*nums[i-1]
            
        for i in range(len(right)-2,-1,-1):
            right[i] = right[i+1]*nums[i+1]
            
        print(left, right)
        
        result = []
        
        for i in range(len(left)):
            result.append(left[i]*right[i])
            
        return result
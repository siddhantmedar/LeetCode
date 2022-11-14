class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = deque()
        
        low, high = 0, len(nums)-1
        
        while low<=high:
            if nums[low]**2 >= nums[high]**2:
                result.appendleft(nums[low]**2)
                low+=1
                
            else:
                result.appendleft(nums[high]**2)
                high-=1
        
        return result
    
#      [-4,-1,0,3,10]
#             __
#         [0, 1,9,16,100]
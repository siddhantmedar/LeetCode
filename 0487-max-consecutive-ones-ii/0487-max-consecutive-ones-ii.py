class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = float("-inf")
        used = False
        i = 0
        
        for j,ele in enumerate(nums):
            if ele==1:
                continue
            else:
                if not used:
                    used = True
                else:
                    res = max(res,j-i)
                    
                    while used:
                        if nums[i] == 0:
                            used = False
                        i+=1
                    used = True
                        
        res = max(res, len(nums)-i)
                    
        return res
    
#         0 1 2 3 4 5 6 7 8 9
#         1 1 0 1 1 0 1 1 1 1
#                             _
#               _
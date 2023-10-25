class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        i = 0
        res = 0
        
        for j, ele in enumerate(nums):
            if j==0 or (j>0 and ele > nums[j-1]):
                continue
            else:
                n = j-i
                
                res+=(n*(n+1))//2
                
                i = j
        
        n = j-i+1       
        res+=(n*(n+1))//2
                
        return res
    
    """
            _
    1 3 5 4 4 6
               _
    """
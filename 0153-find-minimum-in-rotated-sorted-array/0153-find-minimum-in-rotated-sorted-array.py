class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        result = float("inf")
        
        def bs(s,e):
            nonlocal result
            
            if s>e:
                return
            
            if nums[s] < nums[e]:
                result = min(result,nums[s])
                return
            
            m=(s+e)>>1
            
            result = min(result,nums[m])
            
            if nums[s]<=nums[m]: # sorted part
                return bs(m+1,e)
            else:
                return bs(s,m-1)
        
        bs(0,len(nums)-1)
        
        return result
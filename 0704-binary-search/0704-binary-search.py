class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(s,e):
            if s>e:
                return -1
            
            m=(s+e)>>1
            
            if nums[m]==target:
                return m
            
            elif nums[m] > target:
                return bs(s,m-1)
            else:
                return bs(m+1,e)
            
        return bs(0,len(nums)-1)
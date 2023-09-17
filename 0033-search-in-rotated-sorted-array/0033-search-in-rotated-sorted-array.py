class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(s,e):
            if s>e:
                return -1
            
            m = (s+e)>>1
            
            if nums[m] == target:
                return m
            
            if nums[s] <= nums[m]:
                if target >= nums[s] and target < nums[m]:
                    return bs(s,m-1)
                else:
                    return bs(m+1,e)
            
            elif nums[m] <= nums[e]:
                if target > nums[m] and target <= nums[e]:
                    return bs(m+1,e)
                else:
                    return bs(s,m-1)
        
        result = bs(0,len(nums)-1) 
        
        print(result)
        
        return result if result!=None else -1
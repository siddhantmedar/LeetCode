class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = nums[0]
        count = 1
        
        for ele in nums[1:]:
            if ele == c:
                count+=1
                
            else:
                count-=1
                
                if count == 0:
                    c = ele
                    count = 1
                    
        return c
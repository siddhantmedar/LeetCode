class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand, count = nums[0], 1
        
        for ele in nums[1:]:
            if ele == cand:
                count+=1
                
            else:
                count-=1
                
                if count == 0:
                    cand = ele
                    count = 1
                    
        return cand
        
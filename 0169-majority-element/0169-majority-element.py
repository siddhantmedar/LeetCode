class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = nums[0]
        cnt  = 1
        
        for ele in nums[1:]:
            if ele==cand:
                cnt+=1
                
            else:
                cnt-=1
                
                if cnt == 0:
                    cand = ele
                    cnt = 1
                    
        return cand
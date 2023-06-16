class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand, cnt = nums[0], 1
        
        for ele in nums:
            if ele==cand:
                cnt+=1
                
            else:
                cnt-=1
                if cnt==0:
                    cand = ele
                    cnt = 1
                    
        return cand
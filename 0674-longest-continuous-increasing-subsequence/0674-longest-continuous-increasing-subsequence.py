class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result = 0
        pre = float("-inf")
        cnt = 0
        
        for ele in nums:
            if ele>pre:
                cnt+=1
                pre=ele
                
            else:
                result = max(result,cnt)
                cnt = 1
                pre = ele
        
        result = max(result, cnt)
        
        return result
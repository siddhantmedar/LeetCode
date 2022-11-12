class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        
        st = set(nums)
        
        for ele in nums:
            if ele-1 not in st:
                cnt = 0
                
                while ele in st:
                    cnt+=1
                    ele+=1
                    
                result = max(result, cnt)
                
        return result
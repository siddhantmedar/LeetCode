class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        
        result = 0
        
        for ele in nums:
            if ele-1 not in st:
                
                count = 0
                
                while ele in st:
                    count+=1
                    ele+=1
                    
                result = max(result, count)
        
        return result
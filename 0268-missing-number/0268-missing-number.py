class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        st = set([x for x in nums])
        
        for ele in range(len(nums)+1):
            if ele not in st:
                return ele
            
        return -1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp = set()
        
        for ele in nums:
            if ele in mp:
                return True
            
            mp.add(ele)
            
        return False
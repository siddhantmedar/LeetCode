class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        mp = {}
        st = set()
        
        missing, dup = None, None
        
        for ele in nums:
            mp[ele] = 1+mp.get(ele,0)
            if mp[ele] > 1:
                dup = ele
            st.add(ele)
        
        for i in range(1, len(nums)+1):
            if i not in st:
                missing = i
                break
        
        return [dup, missing]
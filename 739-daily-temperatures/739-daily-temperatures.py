class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        st = []
        
        for i in range(len(nums)):
            while st and nums[st[-1]] < nums[i]:
                idx = st.pop()
                res[idx] = i-idx
                
            st.append(i)
        
        return res
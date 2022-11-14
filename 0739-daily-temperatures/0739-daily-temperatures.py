class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        st = []
        
        for i,ele in enumerate(nums):
            while st and nums[st[-1]] < ele:
                idx = st.pop()
                result[idx] = i-idx
                
            st.append(i)
            
        return result
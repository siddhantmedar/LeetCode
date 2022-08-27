class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st = []
        n = len(nums)
        res= [-1]*n
        
        for i in range(2*len(nums)):
            while st and nums[st[-1]%n] < nums[i%n]:
                res[st.pop()%n] = nums[i%n]
                
            st.append(i)
            
        return res
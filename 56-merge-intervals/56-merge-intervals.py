class Solution:
    def merge(self, nums: List[List[int]]) -> List[List[int]]:
        nums.sort(key=lambda x:x[0])
        
        st = [nums[0]]
        
        for start, end in nums[1:]:
            if start <= st[-1][1]:
                last = st.pop()
                
                start = min(last[0], start)
                end = max(last[1], end)
                
            st.append([start,end])
                
                
        return st
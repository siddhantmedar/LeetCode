class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        
        result = [0]*len(temperatures)
        
        for i,ele in enumerate(temperatures):
            if st:
                while st and temperatures[st[-1]] < ele:
                    idx = st.pop()
                    result[idx] = i-idx
                    
            st.append(i)
        
        return result
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        result = [None for _ in range(len(temp))]
        st = []
        for i in range(len(temp)):
            while st and temp[st[-1]] < temp[i]:
                idx = st.pop()
                result[idx] = i-idx
                
            st.append(i)
        
        while st:
            idx = st.pop()
            result[idx] = 0
            
        return result
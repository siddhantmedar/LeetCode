class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        st = []
        
        res = [-1]*len(arr)
        
        for i in range(len(arr)-1,-1,-1):
            if st:
                res[i] = st[-1]
                if arr[i] > st[-1]:
                    st.pop()
                    st.append(arr[i])
            else:
                st.append(arr[i])
            
        return res
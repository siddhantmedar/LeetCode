class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        
        for c in s:
            if not st:
                st.append(c)
            else:
                if st and st[-1] == c:
                    st.pop()
                else:
                    st.append(c)
                    
        return "".join(st)
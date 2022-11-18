class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        
        for c in num:
            if not st or k == 0:
                st.append(c)
                
            else:
                while st and c < st[-1]:
                    st.pop()
                    k-=1
                    if k == 0:
                        break
                st.append(c)
        
        while k:
            if st:
                st.pop()
                k-=1
        
        while st and st[0] == "0":
            st.pop(0)
        
        return "".join(st) if st else "0"
                
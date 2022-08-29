class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1, st2 = [], []
        
        for c in s:
            if c != "#":
                st1.append(c)
            else:
                if st1:
                    st1.pop()
        
        for c in t:
            if c != "#":
                st2.append(c)
            else:
                if st2:
                    st2.pop()
                
        return st1 == st2
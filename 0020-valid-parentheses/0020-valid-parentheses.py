class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        
        for c in s:
            if c in "({[":
                st.append(c)
            else:
                if not st:
                    return False
                
                if st and c==")":
                    if st[-1]=="(":
                        st.pop()
                    else:
                        return False

                if st and c=="}":
                    if st[-1]=="{":
                        st.pop()
                    else:
                        return False
                
                if st and c=="]":
                    if st[-1]=="[":
                        st.pop()
                    else:
                        return False
                
        if st:
            return False
        
        return True
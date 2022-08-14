class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        
        for c in s:
            if c == "[" or c == "(" or c == "{":
                st.append(c)
                
            else:
                if not st:
                    return False
                
                elif st:
                    if c == "]":
                        if st and st[-1] == "[":
                            st.pop()
                        elif not st or st[-1] != "[":
                            return False
                        
                    if c == ")":
                        if st and st[-1] == "(":
                            st.pop()
                        elif not st or st[-1] != "(":
                            return False
                    
                    if c == "}":
                        if st and st[-1] == "{":
                            st.pop()
                        elif not st or st[-1] != "{":
                            return False
                        
        return True if not st else False
                        
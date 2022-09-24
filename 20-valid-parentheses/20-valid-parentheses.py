class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        
        for c in s:
            if c == "(" or c == "[" or c == "{":
                st.append(c)
            
            else:
                if not st:
                    return False
                
                if c == ")":
                    if st and st[-1] == "(":
                        st.pop()
                    else:
                        return False
                elif c == "]":
                    if st and st[-1] == "[":
                        st.pop()
                    else:
                        return False
                elif c == "}":
                    if st and st[-1] == "{":
                        st.pop()
                    else:
                        return False
                    
        return True if not st else False
                    
        
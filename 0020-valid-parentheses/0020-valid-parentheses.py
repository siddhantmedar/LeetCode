class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        
        for c in s:
            if c == "(" or c == "[" or c == "{":
                st.append(c)
                
            else:
                if not st:
                    return False
                
                if c == "}":
                    if st[-1] != "{":
                        return False
                    else:
                        st.pop()
                        
                elif c == "]":
                    if st[-1] != "[":
                        return False
                    else:
                        st.pop()
                        
                elif c == ")":
                    if st[-1] != "(":
                        return False
                    else:
                        st.pop()
                        
        return True if not st else False
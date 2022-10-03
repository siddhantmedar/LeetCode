class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        
        for c in tokens:
            if c == "+" or c == "-" or c == "*" or c == "/":
                if len(st) >= 2:
                    b = st.pop()
                    a = st.pop()
                    
                    if c == "+":
                        st.append(a+b)
                        
                    elif c == "-":
                        st.append(a-b)
                        
                    elif c == "*":
                        st.append(a*b)
                        
                    elif c == "/":
                        result = a/b
                        
                        if result > 0:
                            st.append(floor(result))
                        else:
                            st.append(ceil(result))
                
            else:
                st.append(int(c))
        
        return st[0]
                
        
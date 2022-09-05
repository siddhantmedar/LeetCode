class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        
        for c in tokens:
            if c not in ("+","-","*","/"):
                st.append(int(c))
            else:
                num2 = st.pop()
                num1 = st.pop()
                
                if c == "+":
                    st.append(num1+num2)
                
                elif c == "-":
                    st.append(num1-num2)
                    
                elif c == "*":
                    st.append(num1*num2)
                
                elif c == "/":
                    res = num1/num2
                    
                    if res < 0:
                        st.append(ceil(res))
                    else:
                        st.append(floor(res))

        return st[0]
        
        
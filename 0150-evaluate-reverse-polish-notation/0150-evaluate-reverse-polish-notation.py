class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {"+","-","*","/"}
        st = []

        for c in tokens:
            if c not in op:
                st.append(int(c))
                
            else:
                num2, num1 = st.pop(), st.pop()
                
                if c == "+":
                    st.append(num1+num2)
                elif c == "-":
                    st.append(num1-num2)
                elif c == "*":
                    st.append(num1*num2)
                elif c == "/":
                    result = num1/num2
                    
                    if result < 0:
                        st.append(ceil(result))
                        
                    else:
                        st.append(floor(result))
                        
        return st[0]
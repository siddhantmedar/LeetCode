class Solution:
    def calculate(self, s: str) -> int:
        st = []
        res = 0
        sign = 1
        op = 0
        
        for c in s:
            if c.isdigit():
                op = op*10+int(c)
                
            elif c == "(":
                st.append(res)
                st.append(sign)
                
                sign = 1
                res = 0
                
            elif c == ")":
                res+=op*sign
                res*=st.pop()
                res+=st.pop()
                
                op = 0
            
            elif c == "+":
                res+=sign*op
                
                sign = 1
                op = 0
                
            elif c == "-":
                res+=sign*op
                
                sign = -1
                op = 0
                
        return res+sign*op
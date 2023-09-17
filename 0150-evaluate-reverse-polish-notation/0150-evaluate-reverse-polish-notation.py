class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        
        for c in tokens:
            if c in "+-*/":
                ele2,ele1 = st.pop(),st.pop()
                
                if c=="+": st.append(ele1+ele2)
                if c=="-": st.append(ele1-ele2)
                if c=="*": st.append(ele1*ele2)
                if c=="/": st.append(floor(ele1/ele2) if ele1/ele2 > 0 else ceil(ele1/ele2))
            else:
                st.append(int(c))
                
        return floor(st[-1])
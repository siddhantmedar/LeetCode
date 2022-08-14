class Solution:
    def makeGood(self, s: str) -> str:
        curr = list(s)
        
        while True:
            changed = False
            st = []
            i = 0
            
            while i < len(curr)-1:
                if ord(curr[i])+32  == ord(curr[i+1]) or ord(curr[i]) == ord(curr[i+1])+32:
                    i+=1
                    changed = True
                else:
                    st.append(curr[i])
                
                i+=1
            
            if i < len(curr):
                if st and (ord(curr[i])+32 == ord(st[-1]) or ord(st[-1])+32 == ord(curr[i])):                       st.pop()
                    
                else:
                    st.append(curr[i])
            
            if not changed:
                break
                
            curr = st
            
        return "".join(curr)
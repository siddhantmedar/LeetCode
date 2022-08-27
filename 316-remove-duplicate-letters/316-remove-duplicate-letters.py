class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        st = []
        
        mp = {}
        
        for c in s:
            mp[c] = 1+mp.get(c,0)
            
        for c in s:
            if c in st:
                mp[c]-=1
                continue
                
            if not st:
                mp[c]-=1
                st.append(c)
                
            else:
                while st and st[-1] > c:
                    if mp[st[-1]] >= 1:
                        st.pop()
                    else:
                        break
                
                st.append(c)
                mp[c]-=1
                
        return "".join(st)
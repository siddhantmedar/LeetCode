class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ref = dict()
        mp = dict()
        
        mx = float("inf")
        result = ""
        
        for c in t:
            ref[c] = 1+ref.get(c,0)
            
        i = 0
        
        need = len(ref)
        
        for j in range(len(s)):
            c = s[j]
            
            mp[c] = 1+mp.get(c,0)
            
            if c in ref and mp[c] == ref[c]:
                need-=1
                
            if need == 0:
                while need == 0:
                    if j-i+1 < mx:
                        mx = j-i+1
                        result = s[i:j+1]
                        
                    rm = s[i]

                    mp[rm]-=1

                    if rm in ref and mp[rm] < ref[rm]:
                        need+=1

                    if mp[rm] == 0:
                        del mp[rm]

                    i+=1
        
        if need == 0:
            if len(s)-i < mx:
                mx = len(s)-i
                result = s[i:]
        
        return result                        
        
        # A D O B E C O D E B  A N  C 
        # 0 1 2 3 4 5 6 7 8 9 10 11 12
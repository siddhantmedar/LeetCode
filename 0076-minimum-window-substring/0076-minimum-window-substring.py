class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ref = dict()
        mp = dict()
        
        for c in t:
            ref[c]=1+ref.get(c,0)
            
        need = len(ref)
        
        mx, result = float("inf"), None
        
        i = 0
        
        for j,c in enumerate(s):
            mp[c]=1+mp.get(c,0)
            
            if c in ref and mp[c]==ref[c]:
                need-=1
            
            # shrink
            while need == 0:
                if len(s[i:j+1]) < mx:
                    mx = len(s[i:j+1])
                    result = s[i:j+1]

                char = s[i]
                mp[char]-=1

                if char in ref and mp[char] < ref[char]:
                    need+=1

                if mp[char]==0:
                    del mp[char]

                i+=1
        
        if need==0 and len(s[i:len(s)]) < mx:
            mx = len(s[i:len(s)])
            result = s[i:len(s)]
        
        print(result)
        return result if result!=None else ""
            
        
        # cae 5 
        """
                    _
        cabwefgewcwaefgcf
                         _
        """
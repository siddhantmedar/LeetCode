class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ref = {}
        
        for c in t:
            ref[c] = 1+ref.get(c,0)
            
        need = len(ref)
        mp = {}
        mx, res = float("inf"), None
        i = 0
        
        for j, c in enumerate(s):
            mp[c] = 1+mp.get(c,0)
            
            if c in ref and mp[c] == ref[c]:
                need-=1
                
                while need == 0:
                    if j-i+1 < mx:
                        mx = j-i+1
                        res = s[i:j+1]

                    mp[s[i]]-=1

                    if s[i] in ref and mp[s[i]] < ref[s[i]]:
                        need+=1

                    if mp[s[i]] == 0:
                        del mp[s[i]]

                    i+=1
        
        return res if res else ""

                    
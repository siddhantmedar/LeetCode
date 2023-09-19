class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = dict()
        
        result = 0
        i = 0
        
        for j,c in enumerate(s):
            mp[c]=1+mp.get(c,0)
            
            mx = mp[max(mp,key=mp.get)]
            total = sum(mp.values())
            
            if total-mx<=k:
                result = max(result,total)
                
            else:
                while total-mx>k:
                    print(i)
                    mp[s[i]]-=1
                    i+=1
                    
                    mx = mp[max(mp,key=mp.get)]
                    total = sum(mp.values())
                
                result = max(result,total)
        
        return result
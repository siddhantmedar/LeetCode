class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        mp = {}
        
        i = 0
        for j,c in enumerate(s):
            mp[c] = 1+mp.get(c,0)
            
            length = j-i+1
            mx = max([v for k,v in mp.items()])
            
            if length-mx<=k:
                result = max(result, j-i+1)
                
            else:
                while (j-i+1)-mx > k:
                    mp[s[i]]-=1
                    
                    if mp[s[i]] == 0:
                        del mp[s[i]]
                        
                    i+=1
                    
                result = max(result, j-i+1)
        
        
        return result
            
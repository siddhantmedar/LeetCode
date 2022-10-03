class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        mp = {}
        
        i = 0
        
        for j in range(len(s)):
            ele = s[j]
            mp[ele] = 1+mp.get(ele, 0)
            
            if (j-i+1)-max([v for _,v in mp.items()]) <= k:
                result = max(result,j-i+1)
                
            else:
                while (j-i+1)-max([v for _,v in mp.items()]) > k:
                    mp[s[i]]-=1
                    
                    if mp[s[i]] == 0:
                        del mp[s[i]]
                    
                    i+=1
        
        if (len(s)-i)-max([v for _,v in mp.items()]) <= k:
            result = max(result,len(s)-i)
            
        return result
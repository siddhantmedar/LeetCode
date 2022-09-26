class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        mp = dict()
        
        result = 0
        
        for j in range(len(s)):
            mp[s[j]] = 1+mp.get(s[j], 0)
            
            mx = max([v for _, v in mp.items()])
            
            if (j-i+1) - mx <= k:
                result = max(result, j-i+1)
                
            else:
                while (j-i+1) - mx > k:
                    mp[s[i]]-=1
                    i+=1
            
        if len(s)-i <= k:
            result = max(result, len(s)-i)
            
        print(result)
        
        return result
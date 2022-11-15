class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = float("-inf")
        mp = {}
        i = 0
        
        for j,c in enumerate(s):
            if c not in mp:
                mp[c] = 1+mp.get(c,0)
            
            else:
                result = max(result, j-i)
                
                while c in mp:
                    mp[s[i]]-=1
                    if mp[s[i]] == 0:
                        del mp[s[i]]
                        
                    i+=1
                
                mp[c] = 1+mp.get(c,0)
                    
        result = max(result, len(s)-i)
        
        return result
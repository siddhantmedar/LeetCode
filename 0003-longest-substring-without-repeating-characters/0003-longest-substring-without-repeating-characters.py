class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = dict()
        result = 0
        i = 0
        # s = s.strip()
        
        for j,c in enumerate(s):
            if c not in mp:
                mp[c]=1+mp.get(c,0)
                
            else:
                result = max(result,len(s[i:j]))
                
                while mp[c] != 0:
                    mp[s[i]]-=1
                    i+=1
                    
                mp[c]=1+mp.get(c,0)
                
        return max(result,sum(v for v in mp.values()))
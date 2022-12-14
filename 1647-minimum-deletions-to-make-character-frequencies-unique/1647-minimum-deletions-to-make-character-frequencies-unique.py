class Solution:
    def minDeletions(self, s: str) -> int:
        mp = {}
        
        for c in s:
            mp[c] = 1+mp.get(c,0)
        
        seen = set()
        cnt = 0
        
        for k,v in mp.items():
            while v in seen:
                v-=1
                cnt+=1
                if v == 0:
                    break
                
            if v==0:
                continue
            
            seen.add(v)
            
        return cnt
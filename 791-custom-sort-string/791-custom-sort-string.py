class Solution:
    def customSortString(self, order: str, s: str) -> str:
        mp = {x:0 for x in order}
        misc = ""
        
        for c in s:
            if c in mp:
                mp[c]+=1
                
            else:
                misc+=c
        
        res = ""
        
        for k,v in mp.items():
            while v:
                res+=k
                v-=1
                
        return res+misc
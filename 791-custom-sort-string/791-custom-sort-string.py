class Solution:
    def customSortString(self, order: str, s: str) -> str:
        container = {x:0 for x in order}
        misc = ""
        
        for c in s:
            if c in container:
                container[c]+=1
            else:
                misc+=c
                
        res = ""
        
        for k,v in container.items():
            while v:
                res+=k
                v-=1
                
        return res+misc
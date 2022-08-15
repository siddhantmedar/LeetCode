class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        mp = {}
        tmp = {}
        res = []
        
        i = 0
        
        for c in p:
            mp[c] = 1+mp.get(c,0)
        
        size = 0
        
        for j in range(len(s)):
            c = s[j]
            
            if size < len(p):
                tmp[c] = 1+tmp.get(c,0)
                size+=1
                
            if size == len(p):
                if tmp == mp:
                    res.append(i)
                    
                while size >= len(p):
                    ch = s[i]
                    tmp[ch]-=1
                    size-=1
                    i+=1
                    if not tmp[ch]:
                        del tmp[ch]
            
        if size == len(p) and tmp == mp:
            res.append(i)
          
        return res
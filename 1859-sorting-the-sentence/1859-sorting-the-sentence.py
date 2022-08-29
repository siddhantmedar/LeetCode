class Solution:
    def sortSentence(self, s: str) -> str:
        lst = s.split()
        
        mp = {x:None for x in range(1, len(lst)+1)}

        for word in lst:
            mp[int(word[-1])] = word[:-1]
            
        print(mp)
        
        res = ""
        
        for k,v in mp.items():
            res+=v
            res+=" "
            
        return res[:-1]
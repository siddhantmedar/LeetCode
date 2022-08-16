class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split()
        words2 = s2.split()
        
        mp1 = {}
        mp2 = {}
        
        for word in words1:
            mp1[word] = 1+mp1.get(word,0)
            
        for word in words2:
            mp2[word] = 1+mp2.get(word,0)

        res = []
        
        for k,v in mp1.items():
            if v == 1 and k not in mp2:
                res.append(k)
        
        for k,v in mp2.items():
            if v == 1 and k not in mp1:
                res.append(k)
        
        return res
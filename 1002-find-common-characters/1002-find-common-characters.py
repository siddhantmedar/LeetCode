class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        mp = defaultdict()
        
        for word in words:
            tmp = defaultdict()
            
            for w in word:
                tmp[w] = 1 + tmp.get(w,0)
                mp[(w, tmp[w])] = 1+mp.get((w, tmp[w]), 0)
                
        result = []
        
        for k,v in mp.items():
            if v == len(words):
                result.append(k[0])
                
        return result
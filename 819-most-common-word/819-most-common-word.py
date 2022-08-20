class Solution:
    def mostCommonWord(self, s: str, banned: List[str]) -> str:
        word = ""
        lst = []
        
        for c in s:
            if c.isalpha():
                word+=c
                
            elif c == "!" or c == "?" or c == "," or c == "," or c == "." or c == " ":
                if word:
                    lst.append(word.lower())
                    word=""
        if word:
            lst.append(word.lower())
            
        print(lst)
        
        st = set(banned)
        
        mp = {}
        
        for word in lst:
            mp[word] = 1+mp.get(word, 0)
            
        mp = list(mp.items())
        
        mp.sort(key=lambda x:-x[1])
        print(mp)
        for k,v in mp:
            if k in st:
                continue
            else:
                return k
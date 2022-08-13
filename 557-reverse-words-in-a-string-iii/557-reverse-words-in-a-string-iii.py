class Solution:
    def reverseWords(self, s: str) -> str:
        def rev(st):
            start, end = 0, len(st)-1
            tmp = list(st)
            
            while start <= end:
                tmp[start], tmp[end] = tmp[end], tmp[start]
                start+=1
                end-=1
            
            return "".join(tmp)
        
        word = ""
        res = ""
        
        for c in s:
            if c != " ":
                word+=c
            
            elif c == " ":
                if word:
                    word = rev(word)
                    res+=word
                    res = res+c
                    word = ""
                    
        if word:
            word = rev(word)
            res+= word
            word=""
            
        return res
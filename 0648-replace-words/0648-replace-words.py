class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)
        result = []
        
        for word in sentence.split():
            s = ""
            rep = None
            
            for c in word:
                s+=c
                if s in dictionary:
                    rep = s
                    break
            
            print(s,rep)
            result.append(rep if rep else s)
            
        return " ".join(result)
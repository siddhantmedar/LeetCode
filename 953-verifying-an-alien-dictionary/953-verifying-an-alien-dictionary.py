class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordering = dict()
        
        for i, c in enumerate(order):
            ordering[c] = i
            
        print(ordering)
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            
            mn = min(len(w1), len(w2))
            
            if len(w1) > len(w2) and w1[:mn] == w2[:mn]:
                return False
        
            for i, (c1, c2) in enumerate(zip(w1,w2)):
                if ordering[c1] < ordering[c2]:
                    break
                
                elif ordering[c1] > ordering[c2]:
                    return False

        return True
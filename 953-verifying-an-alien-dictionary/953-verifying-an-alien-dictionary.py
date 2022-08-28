class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pattern = {}
        
        for i, c in enumerate(order):
            pattern[c] = i
            
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            mn = min(len(word1), len(word2))
            
            if len(word1) > len(word2) and word1[:mn] == word2[:mn]:
                return False
            
            for j in range(mn):
                if pattern[word1[j]] < pattern[word2[j]]:
                    break
                    
                elif pattern[word1[j]] > pattern[word2[j]]:
                    return False
                
        return True
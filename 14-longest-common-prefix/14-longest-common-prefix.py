class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = min(strs)
        result = ""
        
        for i,c in enumerate(word):
            valid = True
            
            for words in strs:
                if words == word:
                    continue
                    
                if words[i] != c:
                    valid = False
                    
            if valid:
                result+=c
                
            else:
                break
                
                
        return result
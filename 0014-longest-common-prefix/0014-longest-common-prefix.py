class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref = None
        best = float("inf")
        
        for word in strs:
            if len(word) < best:
                best = len(word)
                ref = word
        
        result = ""
        
        for i,c in enumerate(ref):
            valid = True 
            
            for word in strs:
                if word[i] != c:
                    valid = False
                    
            if valid:
                result+=c
            else:
                break
                
        return result
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        
        ref = {}
        
        for c in chars:
            ref[c] = 1+ref.get(c,0)
        
        for word in words:
            mp = {}
            valid = True
            
            for c in word:
                if c not in ref:
                    valid = False
                    break
                
                mp[c] = 1+mp.get(c,0)
                
                if mp[c] > ref[c]:
                    valid = False
                    break
                    
            if valid:
                result+=len(word)
                
        return result
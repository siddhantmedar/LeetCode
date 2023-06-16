class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mn = min(strs)
        k = len(mn)
        
        res = ""
        
        for i,c in enumerate(mn):
            valid = True
            
            for word in strs:
                if word != mn and word[i] != c:
                    valid = False
                    
            if valid:
                res+=c
                
            else:
                break
                
        return res
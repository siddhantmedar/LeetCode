class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = min(strs)
        
        res = ""
        
        for i, c in enumerate(word):
            count = 0
            for w in strs:
                if w[i] == c:
                    count+=1
                    
            if count == len(strs):
                res+=c
            
            else:
                break
            
        return res
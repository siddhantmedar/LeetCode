class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(idx, res):
            if idx == len(digits):
                if res:
                    result.append(res)
                return
            
            
            s = mp[digits[idx]]
            
            for c in s:
                dfs(idx+1, res+c)
            
            
        mp = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        result = []
        
        dfs(0,"")
        
        return result
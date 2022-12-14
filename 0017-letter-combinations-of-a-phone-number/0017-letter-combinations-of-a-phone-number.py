class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def solve(idx,path):
            if idx == len(digits):
                result.append(path)
                return
            
            curr = mp[digits[idx]]
            
            for c in curr:
                solve(idx+1,path+c)
            
        
        mp = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
           "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        if not digits:
            return []
        
        result = []
        
        solve(0,"")
        
        return result
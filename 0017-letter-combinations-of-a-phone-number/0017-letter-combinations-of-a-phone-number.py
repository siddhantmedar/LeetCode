class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def solve(idx,path):
            if idx == len(digits):
                if path:
                    result.append(path[:])
                return
            
            s = mp[digits[idx]]
            
            for c in s:
                solve(idx+1,path+c)
        
        
        mp = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
           "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        result = []
        
        solve(0,"")
        
        return result
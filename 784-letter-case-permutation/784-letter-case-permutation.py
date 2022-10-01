class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def solve(idx, res):
            if idx >= len(s):
                result.append(res)
                return
            
            if s[idx].isalpha():
                solve(idx+1, res+s[idx].upper())
                solve(idx+1, res+s[idx].lower())
            else:
                solve(idx+1, res+s[idx])
            
        result = []
        
        solve(0,"")
        
        return result
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solve(open, close, res):
            if open == n and close == n:
                result.append(res)
                return
            
            if open < n:
                solve(open+1, close, res+"(")
                
            if close < open:
                solve(open, close+1, res+")")
                
        
        result = []
        
        solve(0,0,"")
        
        return result
        
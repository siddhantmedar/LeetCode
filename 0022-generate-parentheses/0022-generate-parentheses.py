class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solve(open,close,path):
            if len(path) == 2*n:
                result.append(path)
                return
            
            if open < n:
                solve(open+1,close,path+"(")
                
            if close < open:
                solve(open,close+1,path+")")
                
                
        result = []
        
        solve(0,0,"")
        
        return result
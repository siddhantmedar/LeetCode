class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solve(o,c,path):
            nonlocal result
            
            if o==n and c==n:
                result.append(path[::])
                return
            
            if o < n:
                solve(o+1,c,path+"(")
            
            if o>c:
                solve(o,c+1,path+")")
        
        
        result = []
        solve(0,0,"")
        
        print(result)
        
        return result
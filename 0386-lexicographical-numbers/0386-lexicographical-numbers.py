class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(i):
            nonlocal result
            
            if i > n:
                return
            
            result.append(i)
            
            for j in range(10):
                dfs(i*10+j)
                
        
        result = []
        
        for i in range(1,10):
            dfs(i)
        
        return result
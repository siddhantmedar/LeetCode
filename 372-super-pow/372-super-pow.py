class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def solve(b):
            if b == 1:
                return a
            
            elif b == 0:
                return 1
            
            res = solve(b//2)
            
            if b%2 == 0:
                return res*res % 1337
            else:
                return a*res*res % 1337
        
        b = int("".join([str(x) for x in b]))
        
        return solve(b) % 1337
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalin(i ,j):
            x = s[i:j+1]
            return x == x[::-1]
    
        def solve(idx):
            nonlocal result, tmp
            
            if idx >= len(s):
                result.append(tmp[:])
                return
            
            for k in range(idx, len(s)):
                if isPalin(idx,k):
                    tmp.append(s[idx:k+1])
                    
                    solve(k+1)

                    tmp.pop()

        
        tmp = []
        result = []
        
        solve(0)
        
        return result

    
# a|bcb
# 0 123
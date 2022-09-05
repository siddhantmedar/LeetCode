class Solution:
    def countPrimes(self, n: int) -> int:
        def sieve(n):
            res = [0 for _ in range(n)]
            
            for i in range(3, len(res), 2):
                res[i] = 1
                
            for i in range(3, len(res)):
                if res[i]:
                    for j in range(i*i, len(res), i):
                        res[j] = 0
            
            if 2 < len(res):
                res[2] = 1
            
            return res.count(1)
            
        return sieve(n)
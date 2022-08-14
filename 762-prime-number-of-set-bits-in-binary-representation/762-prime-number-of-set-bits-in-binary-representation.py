class Solution:
    def countPrimeSetBits(self, l: int, r: int) -> int:
        def issetPrime(n):
            count = 0
            
            while n:
                count+=(n&1)
                n>>=1
                
            return count in st
            
        st = set([2,3,5,7,11,13,17,19])
        
        count = 0
        
        for i in range(l,r+1):
            if issetPrime(i):
                count+=1
                
        return count
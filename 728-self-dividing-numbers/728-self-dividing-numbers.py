class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def selfDiv(n):
            div = set()
            tmp = n
            
            while n > 0:
                div.add(n%10)
                n//=10
            
            if 0 in div:
                return False
            
            if all(tmp % i == 0 for i in div):
                return True
            else:
                return False
            
        res = []
        
        for i in range(left, right+1):
            if selfDiv(i):
                res.append(i)
        
        return res
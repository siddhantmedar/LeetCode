class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def check(n):
            while n:
                if n%10==0:
                    return False
                n//=10
                
            return True
        
        
        tmp = []
        
        for num in range(1,n):
            if check(num):
                tmp.append(num)
        
        for i in range(len(tmp)):
            for j in range(len(tmp)):
                if tmp[i]+tmp[j]==n:
                    return [tmp[i],tmp[j]]
        
        
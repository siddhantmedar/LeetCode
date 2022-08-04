class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def getSetBits(n):
            count = 0
            
            while n:
                count+=(n&1)
                n>>=1
                
            return count
        
        tmp = []
        
        for ele in arr:
            tmp.append((getSetBits(ele),ele))
            
        tmp.sort(key=lambda x:(x[0],x[1]))
        
        res = []
        
        for count, ele in tmp:
            res.append(ele)
            
        return res
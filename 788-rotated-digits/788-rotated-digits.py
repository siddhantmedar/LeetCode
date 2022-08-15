class Solution:
    def rotatedDigits(self, n: int) -> int:
        def getMirrored(n):
            s=""
            
            for c in str(n):
                if mp[int(c)] == None:
                    return False
                s+=str(mp[int(c)])
            
            return int(s) != n
            
        mp ={0:0,
             1:1,
             2:5,
             3:None,
             4:None,
             5:2,
             6:9,
             7:None,
             8:8,
             9:6}
        
        count = 0
        
        for i in range(1, n+1):
            if getMirrored(i):
                count+=1
                
        return count
        
        
#         1 2 3 4 5 6 7 8 9 0
#         x 5 x x 2 9 x x 6 x
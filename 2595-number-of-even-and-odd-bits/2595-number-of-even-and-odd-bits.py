class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        odd,even = 0, 0
        
        for i in range(32):
            if i%2==0:
                if n&1:
                    even+=1
            else:
                if n&1:
                    odd+=1
                    
            n>>=1
            
        return [even, odd]
            
                
        
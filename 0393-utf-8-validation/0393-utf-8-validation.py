class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        rem = 0
        
        for ele in data:
            if rem == 0:
                if ele>>7 == 0b0:
                    rem = 0
                    
                elif ele>>5 == 0b110:
                    rem = 1
                    
                elif ele>>4 == 0b1110:
                    rem = 2
                    
                elif ele>>3 == 0b11110:
                    rem = 3
                else:
                    return False
                    
            else:
                if ele>>6 == 0b10:
                    rem-=1
                else:
                    return False
                    
        return True if rem == 0 else False
               
# 0
# 110
# 1110
# 11110

# 01
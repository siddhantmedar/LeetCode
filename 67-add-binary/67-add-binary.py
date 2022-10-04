class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        
        idx1, idx2 = len(a)-1, len(b)-1
        
        while idx1 >= 0 or idx2 >= 0:
            x = a[idx1] if idx1 >= 0 else "0"
            y = b[idx2] if idx2 >= 0 else "0"
            
            if x == "0" and y == "0":
                if carry:
                    result = "1"+result
                    carry = 0
                    
                else:
                    result = "0"+result
                    
            elif x == "0" and y == "1":
                if carry:
                    result = "0"+result
                    carry = 1
                    
                else:
                    result = "1"+result
                    
            elif x == "1" and y == "0":
                if carry:
                    result = "0"+result
                    carry = 1
                    
                else:
                    result = "1"+result
                    
            elif x == "1" and y == "1":
                if carry:
                    result = "1"+result
                    
                else:
                    result = "0"+result
                    
                carry = 1
            
            idx1-=1
            idx2-=1
            
        if carry:
            result = str(carry)+result
        
        # print(result)
            
        return result
        
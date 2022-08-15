class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        
        if num1 == 0 or num2 == 0:
            return count
        
        while num1 != 0 or num2 != 0:
            if num1 >= num2:
                num1-=num2
                count+=1
                
                if num1 == 0:
                    return count
                
            else:
                num2-=num1
                count+=1
                
                if num2 == 0:
                    return count
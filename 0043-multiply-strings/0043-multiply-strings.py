class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = deque([0]*(len(num1)+len(num2)))
        
        ptr = len(result)-1
        carry = 0
        
        for j in range(len(num2)-1,-1,-1):
            k = ptr
            for i in range(len(num1)-1,-1,-1):
                ans = int(num2[j])*int((num1[i])) + carry
                
                carry = ans//10
                
                val = result[k]+(ans%10)
                result[k] = val%10
                carry += val//10
                
                k-=1
                
            if carry:
                result[k] += carry
                carry = 0
                
            ptr-=1
        
        while result and result[0] == 0:
            result.popleft()
            
        if not result:
            return "0"
        
        return "".join([str(x) for x in result])
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = deque([0 for _ in range(len(num1)+len(num2))])
        
        ptr = len(result)-1
        
        carry = 0
        
        for i in range(len(num2)-1, -1, -1):
            b = int(num2[i])
            idx = ptr
            
            for j in range(len(num1)-1, -1, -1):
                a = int(num1[j])
                
                product = a*b + carry
                
                carry = (product // 10)
                
                carry += (result[idx] + (product % 10)) // 10
                
                result[idx] = (result[idx] + (product % 10)) % 10
                
                idx-=1
            
            if carry:
                result[idx] += carry
                carry = 0
                
            ptr-=1
            
        print(result)
        
        while result and result[0] == 0:
            result.popleft()
        
        return "".join([str(x) for x in result]) if result else "0"
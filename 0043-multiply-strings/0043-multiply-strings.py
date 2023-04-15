class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        p1,p2 = len(num1), len(num2)
        
        res = [0 for _ in range(p1+p2)]
        
        ptr = len(res)
        carry = 0
        
        for j in range(len(num2)-1,-1,-1):
            ptr-=1
            tmp = ptr
            
            for i in range(len(num1)-1,-1,-1):
                a = int(num2[j])
                b = int(num1[i])
                
                sm = a*b + carry + res[tmp]
                
                carry = sm // 10
                res[tmp] = sm %10
                
                tmp-=1
                
            if carry:
                res[tmp] = carry
                carry = 0
                
        print(res)
        
        res = "".join([str(x) for x in res])
        
        idx = 0 
        
        while idx < len(res) and res[idx] == "0":
            idx+=1
            
        if idx == len(res):
            return "0"
        
        return res[idx:]
                
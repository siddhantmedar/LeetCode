class Solution:
    def isHappy(self, n: int) -> bool:
        st = set()
        
        while n != 1:
            tmp = 0
            
            while n:
                tmp+=(n%10)**2
                n//=10
                
            n = tmp
            
            if n in st:
                break
            
            st.add(n)
            
        return True if n==1 else False
            
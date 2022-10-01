class Solution:
    def reverse(self, x: int) -> int:
        def solve(n):
            if n>0:
                return str(n%10) + solve(n//10)
            
            return ""
        
        if x != 0:
            neg = True if x < 0 else False

            result = int(solve(abs(x)))

            result = -1*result if neg else result

            if -2**31 <= result <= 2**31-1:
                return result

            return 0
            
        else:
            return 0
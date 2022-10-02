class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        def solve1(n):
            if n>0:
                tmp = n%10
                solve1(n//10)   
                lst1.append(tmp)

        def solve2(n):
            if n>0:
                lst2.append(n%10)
                solve2(n//10)
        
        lst1, lst2 = [], []
        
        solve1(x)
        solve2(x)
        
        # print(lst1, lst2)
        
        return lst1 == lst2
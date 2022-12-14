class Solution:
    def maxValue(self, n: str, x: int) -> str:
        def solve1(lst,x):
            inserted = False
            res = ""
            
            for c in n:
                if str(x) > c and not inserted:
                    res+=str(x)+c
                    inserted = True
                else:
                    res+=c
            
            if not inserted:
                return "".join(lst+[str(x)])
            
            return res
        
        
        def solve2(lst,x):
            inserted = False
            res = ""
            
            for c in n:
                if str(x) < c and not inserted:
                    res+=str(x)+c
                    inserted = True
                else:
                    res+=c
            
            if not inserted:
                return "-"+"".join(lst+[str(x)])
            
            return "-"+res
        
            
        neg = False
        
        if n[0] == "-":
            neg = True
            n=n[1:]
        
        if not neg:
            return solve1(list(n),x)
        else:
            return solve2(list(n),x)
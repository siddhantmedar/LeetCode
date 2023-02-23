class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gaved = set()
        res = 0
        
        for b in s:
            for i in range(len(g)):
                if b >= g[i] and i not in gaved:
                    gaved.add(i)
                    res+=1
                    break
            
        return res
    
    
    # [1 2 3]  [3,1,2]
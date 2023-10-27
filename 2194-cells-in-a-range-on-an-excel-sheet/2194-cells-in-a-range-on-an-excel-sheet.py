class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        s,e = s.split(":")
        
        res = []
        
        for i in range(ord(s[0]), ord(e[0])+1):
            for j in range(int(s[1]), int(e[1])+1):
                res.append(chr(i)+str(j))
                
        return res
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        mp = {
            "U":(0,1),
            "R":(1,0),
            "L":(-1,0),
            "D":(0,-1)
        }
        
        i,j = 0, 0
        
        for m in moves:
            i+=mp[m][0]
            j+=mp[m][1]
        
        return i == 0 and j == 0
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) != len(s):
            return False
        
        tmp = s
        
        for i in range(len(s)-1):
            tmp = tmp[1:]+tmp[0]
            
            if tmp == goal:
                return True
            
        return False
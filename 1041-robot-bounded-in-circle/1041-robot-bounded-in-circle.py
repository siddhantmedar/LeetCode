class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dir = [(0,1), (1,0), (0,-1), (-1,0)]
                    
        #two conditions needs to be checked if after one iteration
        # does the robot return to the origin?
        # not facing north?
        
        #if either of these, then bounded in circle else not
        
        
        i,j = 0, 0
        idx = 0

        for c in instructions:
            if c == "L":
                idx = (idx+3)%4
                
            elif c == "R":
                idx = (idx+1)%4
                
                
            else:
                i+=dir[idx][0]
                j+=dir[idx][1]
                
        return (i == 0 and j == 0) or idx != 0
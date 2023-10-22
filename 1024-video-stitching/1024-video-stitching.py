class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        cnt = 0
        mn, mx = 0, 0
        
        while mx < time:
            
            for i in range(len(clips)):
                start, end = clips[i]
                
                if start <= mn and end > mx:
                    mx = end
            
            if mn == mx:
                return -1
            
            mn = mx
            
            cnt+=1
            
        return cnt
            
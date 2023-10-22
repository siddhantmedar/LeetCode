class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        cnt = 0
        mn, mx = 0, 0
        
        while mn < n:
            changed = False
            
            for i in range(len(ranges)):
                start, end = i-ranges[i], i+ranges[i]
                
                if start <= mn and end > mx:
                    changed = True
                    mx = end
            
            if mn == mx:
                return -1
            
            mn = mx
            
            if changed:
                cnt+=1

        return cnt if cnt > 0 else -1
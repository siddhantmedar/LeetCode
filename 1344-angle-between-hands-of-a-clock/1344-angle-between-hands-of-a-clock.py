class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = (hour*60 + minutes)/60
        if h>=12:
            h-=12
        
        h *= 30
        m = minutes*6
        
        print(h,m)
        res = abs(h-m)
        
        if res > 180:
            return abs(360-res)

        return res

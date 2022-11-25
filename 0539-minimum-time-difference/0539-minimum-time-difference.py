class Solution:
    def findMinDifference(self, points: List[str]) -> int:
        def convert(time):
            hr,mn = int(time[:2]),int(time[3:])
            
            hr = 24 if hr == 0 else hr
            return hr*60+mn
        
        
        lst = sorted([convert(x) for x in points])
        
        result = 1440+lst[0]-lst[-1]
        
        for i in range(len(lst)-1):
            result = min(result,lst[i+1]-lst[i])
            
        return result
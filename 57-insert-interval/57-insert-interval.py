class Solution:
    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:
        result = []
        
        for e in intervals:
            if e[1] < new[0]:
                result.append(e)
        
            elif e[0] > new[1]:
                result.append(new)
                new = e
            
            else:
                new[0] = min(new[0], e[0])
                new[1] = max(new[1], e[1])
                
        result.append(new)
        
        return result
class Solution:
    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:
        result = []
        
        for start,end in intervals:
            if end < new[0]:
                result.append([start, end])

            elif start > new[1]:
                result.append(new)
                new = [start, end]
                
            else:
                new[0] = min(new[0], start)
                new[1] = max(new[1], end)
                
        result.append(new)
        
        return result
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        st = [intervals[0]]
        
        for start, end in intervals[1:]:
            if start <= st[-1][1]:
                last = st.pop()
                start = min(start,last[0])
                end = max(end, last[1])
            
            st.append([start, end])
        
        return st
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        
        st = [intervals[0]]
        
        for e in intervals[1:]:
            if st and st[-1][1] >= e[0]:
                last = st.pop()
                
                start = min(last[0], e[0])
                end = max(last[1], e[1])
                
                st.append([start, end])
            
            else:
                st.append(e)
                
        print(st)
        
        return st
        
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        
        heap = [intervals[0][1]]
        
        for start, end in intervals[1:]:
            if heap and heap[0] > start:
                heapq.heappush(heap, end)
                
            else:
                heapq.heappushpop(heap, end)
        
        return len(heap)
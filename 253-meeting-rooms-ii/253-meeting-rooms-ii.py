class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        
        heap = []
        
        for s,e in intervals:
            if not heap:
                heapq.heappush(heap, e)
                
            else:
                if heap[0] <= s:
                    heapq.heappop(heap)
                
                heapq.heappush(heap,e)
                    
        return len(heap)
        
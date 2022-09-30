class Solution:
    def minMeetingRooms(self, nums: List[List[int]]) -> int:
        nums.sort(key = lambda x:x[0])
        
        heap = []
        
        for start, end in nums:
            if not heap:
                heapq.heappush(heap, end)
                
            else:
                if heap[0] <= start:
                    heapq.heappushpop(heap, end)
                
                else:
                    heapq.heappush(heap, end)
        
        return len(heap)
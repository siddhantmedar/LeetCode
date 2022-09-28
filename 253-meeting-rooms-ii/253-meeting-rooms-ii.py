class Solution:
    def minMeetingRooms(self, nums: List[List[int]]) -> int:
        nums.sort()
        
        heap = []
        
        for i in nums:
            if not heap:
                heapq.heappush(heap, i[1])
                
            else:
                if heap[0] <= i[0]:
                    heapq.heappushpop(heap,i[1])
                    
                else:
                    heapq.heappush(heap, i[1])
        
        return len(heap)
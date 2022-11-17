class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        
        for ele in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap,ele)
                
            else:
                if ele > self.heap[0]:
                    heapq.heappushpop(self.heap,ele)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap,val)
            
        else:
            if val > self.heap[0]:
                heapq.heappushpop(self.heap,val)
        
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
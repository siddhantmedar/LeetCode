class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        
        for i in range(min(len(nums),k)):
            self.heap.append(nums[i])
        
        heapq.heapify(self.heap)
        
        for i in range(k, len(nums)):
            if self.heap[0] < nums[i]:
                heapq.heappushpop(self.heap, nums[i])
                

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif len(self.heap) == self.k:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
class MedianFinder:

    def __init__(self):
        self.mx_heap = []
        self.mn_heap = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.mx_heap, -1*num)
        
        heapq.heappush(self.mn_heap, -1*heapq.heappop(self.mx_heap))
        
        while len(self.mn_heap) > len(self.mx_heap):
            heapq.heappush(self.mx_heap, -1*heapq.heappop(self.mn_heap))

    def findMedian(self) -> float:
        if len(self.mx_heap) == len(self.mn_heap):
            return ((-1*self.mx_heap[0]) + self.mn_heap[0]) / 2
        
        elif len(self.mx_heap) > len(self.mn_heap):
            return -1*self.mx_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
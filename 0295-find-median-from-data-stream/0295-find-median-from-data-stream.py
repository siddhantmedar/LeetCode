class MedianFinder:

    def __init__(self):
        self.mx = []
        self.mn = []
    def addNum(self, ele: int) -> None:
        heapq.heappush(self.mx, -ele)
        heapq.heappush(self.mn, -heapq.heappop(self.mx))
        
        while len(self.mn) > len(self.mx):
            heapq.heappush(self.mx, -heapq.heappop(self.mn))
        
    def findMedian(self) -> float:
        if len(self.mx) > len(self.mn):
            return -self.mx[0]
        
        else:
            return (-self.mx[0] + self.mn[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
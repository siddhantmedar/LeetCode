class MedianFinder:

    def __init__(self):
        self.mx = []
        self.mn = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.mx, num)
        
        heapq.heappush(self.mn, -1*heapq.heappop(self.mx))
        
        while len(self.mn) > len(self.mx):
            heapq.heappush(self.mx, -1*heapq.heappop(self.mn))
        
    def findMedian(self) -> float:
        if len(self.mx) > len(self.mn):
            return self.mx[0]
        
        else:
            return (self.mx[0]+(-1*self.mn[0]))/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
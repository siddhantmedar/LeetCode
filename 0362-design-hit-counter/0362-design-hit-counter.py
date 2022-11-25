class HitCounter:

    def __init__(self):
        self.mp = {}
        
    def hit(self, timestamp: int) -> None:
        self.mp[timestamp] = 1+self.mp.get(timestamp,0)

    def getHits(self, timestamp: int) -> int:
        result = 0
        
        for k in list(self.mp):
            if timestamp-k<300:
                result+=self.mp[k]
            else:
                del self.mp[k]
        
        return result

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        lst = self.mp[key]
        
        result = ""
        
        start, end = 0, len(lst)-1
        
        while start <= end:
            mid = (start+end)>>1
            
            if lst[mid][0] <= timestamp:
                result = lst[mid][1]
                start = mid+1
                
            else:
                end = mid-1
                
        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
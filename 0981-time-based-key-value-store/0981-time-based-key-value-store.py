class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[(key)].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.mp[key]
        
        l,r = 0, len(lst)-1
        
        result = None
        
        while l<=r:
            m = (l+r)>>1
            
            if lst[m][0] == timestamp:
                return lst[m][1]
            
            elif lst[m][0] < timestamp:
                result = lst[m][1]
                l=m+1
            else:
                r=m-1
        
        print(result)
        return result if result else ""
    
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
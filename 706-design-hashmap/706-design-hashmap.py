class MyHashMap:
    def __init__(self):
        self.st = [None]*(10**6+1)
        
    def put(self, key: int, value: int) -> None:
        if self.st[key]:
            self.st[key][1] = value
        else:
            self.st[key] = [key, value]
            
            
    def get(self, key: int) -> int:
        if self.st[key]:
            return self.st[key][1]
        else:
            return -1
        

    def remove(self, key: int) -> None:
        if self.st[key]:
            self.st[key] = None
            
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
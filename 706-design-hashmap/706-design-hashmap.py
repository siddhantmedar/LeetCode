class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None

class MyHashMap:
    def addNode(self, node):
        ref = self.head.next
        pre = ref.pre
        
        self.head.next = node
        node.pre = self.head
        
        node.next = ref
        ref.pre = node
        
    def removeNode(self, node):
        pre = node.pre
        nxt = node.next
        
        pre.next = nxt
        nxt.pre = pre
    
    def __init__(self):
        self.st = [None]*(10**6+1)
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        
        self.head.next = self.tail
        self.tail.pre = self.head
        
    def put(self, key: int, value: int) -> None:
        if self.st[key]:
            self.st[key].val = value
        else:
            self.st[key] = ListNode(key, value)
            self.addNode(self.st[key])
            
            
    def get(self, key: int) -> int:
        if self.st[key]:
            return self.st[key].val
        else:
            return -1
        

    def remove(self, key: int) -> None:
        if self.st[key]:
            self.removeNode(self.st[key])
            self.st[key] = None
            
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
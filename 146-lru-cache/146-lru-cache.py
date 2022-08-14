class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

class LRUCache:
    def addNode(self, key, val):
        node = Node(key, val)
        
        ref = self.head.next
        
        node.pre = self.head
        node.next = ref
        
        self.head.next = node
        ref.pre = node
        
        return node
        
    def deleteNode(self, node):
        preref = node.pre
        nxtref = node.next
        
        preref.next = nxtref
        nxtref.pre = preref
        
    def __init__(self, capacity: int):
        self.mp = {}
        self.cap = capacity
        self.size = 0
        
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key in self.mp:
            result = self.mp[key].val
            
            value = self.mp[key].val
            
            self.deleteNode(self.mp[key])
            del self.mp[key]
            
            self.mp[key] = self.addNode(key,value)
            
            return result
        
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.deleteNode(self.mp[key])
            del self.mp[key]
            
            self.mp[key] = self.addNode(key, value)
            
        else:
            if self.size == self.cap:
                k = self.tail.pre.key
                self.deleteNode(self.tail.pre)
                del self.mp[k]
                self.size-=1
            
            self.mp[key] = self.addNode(key,value)
            
            self.size+=1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
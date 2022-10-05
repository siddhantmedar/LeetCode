class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None
        
        self.mp = dict()
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp = {}
        
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        
        self.head.next = self.tail
        self.tail.pre = self.head
    
        
    def addNode(self, node):
        ref = self.head.next
        
        self.head.next = node
        
        node.pre = self.head
        node.next = ref
        
        ref.pre = node
        
    def removeNode(self, node):
        pre = node.pre
        nxt = node.next
        
        pre.next = nxt
        nxt.pre = pre
        
    def get(self, key: int) -> int:
        if key in self.mp:
            result = self.mp[key].val
            
            self.removeNode(self.mp[key])
            del self.mp[key]
            
            node = Node(key, result)
            
            self.addNode(node)
            self.mp[key] = node
            
            return result
            
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.removeNode(self.mp[key])
            del self.mp[key]
            
            node = Node(key,value)
            self.mp[key] = node
            
            self.addNode(node)
            
        else:
            if len(self.mp) == self.capacity:
                rm = self.tail.pre.key
                self.removeNode(self.tail.pre)
                del self.mp[rm]
                
            node = Node(key,value)
            self.mp[key] = node
            self.addNode(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
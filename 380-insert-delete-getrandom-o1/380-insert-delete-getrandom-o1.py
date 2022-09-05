class Node:
    def __init__(self,val):
        self.val = val
        self.pre = None
        self.next = None
    
class RandomizedSet:

    def __init__(self):
        self.mp = {}
        
        self.head = Node(-1)
        self.tail = Node(-1)
        
        self.head.next = self.tail
        self.tail.pre = self.head
    
    
    def addNode(self,node):
        ref = self.head.next
        
        self.head.next = node
        node.pre = self.head
        
        ref.pre = node
        node.next = ref
        
    def removeNode(self, node):
        pre = node.pre
        nxt = node.next
        
        pre.next = nxt
        nxt.pre = pre
        
    def insert(self, val: int) -> bool:
        if val in self.mp:
            return False
        else:
            node = Node(val)
            self.mp[val] = node
            self.addNode(node)
            return True
    
    def remove(self, val: int) -> bool:
        if val in self.mp:
            self.removeNode(self.mp[val])
            del self.mp[val]
            return True
        else:
            return False
    

    def getRandom(self) -> int:
        return self.mp[random.choice(list(self.mp.keys()))].val


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None
        self.cnt = 1
        
class LinkedList:
    def __init__(self):
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        
        self.head.next = self.tail
        self.tail.pre = self.head 
        
        self.size = 0
        
    def addNode(self, node):
        ref = self.head.next
        
        node.pre = self.head
        self.head.next = node
        
        node.next = ref
        ref.pre = node
        
        self.size+=1
    
    def removeNode(self, node):
        pre = node.pre 
        nxt = node.next
        
        pre.next = nxt
        nxt.pre = pre
        
        self.size-=1
        
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp = defaultdict()
        self.freq_mp = defaultdict(LinkedList)
        self.mn_freq = 0
        self.size = 0
        
    def updateFrequencyList(self, node):
        del self.mp[node.key]
        
        lst = self.freq_mp.get(node.cnt)
        
        lst.removeNode(node)
        
        if node.cnt == self.mn_freq and self.freq_mp[self.mn_freq].size == 0:
            self.mn_freq+=1
            
        nxtFreqList = self.freq_mp.get(node.cnt+1, LinkedList())
        
        nxtFreqList.addNode(node)
        
        node.cnt+=1
        
        self.freq_mp[node.cnt] = nxtFreqList
        
        self.mp[node.key] = node
        
    def get(self, key: int) -> int:
        if key in self.mp:
            node = self.mp[key]
            result = node.val
            
            self.updateFrequencyList(node)
            
            return result
        
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.mp:
            self.mp[key].val = value
            self.updateFrequencyList(self.mp[key])
        
        else:
            if self.size == self.capacity:
                lst = self.freq_mp[self.mn_freq]
                del self.mp[lst.tail.pre.key]
                self.freq_mp[self.mn_freq].removeNode(lst.tail.pre)
                self.size-=1

            self.size+=1
            self.mn_freq = 1

            tmp = self.freq_mp.get(self.mn_freq, LinkedList())

            node = Node(key, value)
            tmp.addNode(node)
            self.freq_mp[self.mn_freq] = tmp
            self.mp[key] = node
        
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
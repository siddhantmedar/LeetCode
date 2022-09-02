class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class Bucket:
    def __init__(self):
        self.head = Node(-1)
    
    def nodeExists(self, key):
        tmp = self.head

        while tmp:
            if tmp.val == key:
                return True

            tmp = tmp.next

        return False

    def addNode(self, key):
        if not self.nodeExists(key):
            newNode = Node(key)
            newNode.next = self.head.next
            self.head.next = newNode
    
    def removeNode(self, key):
        if self.nodeExists(key):
            pre = self.head
            curr = self.head.next
            
            while curr:
                if curr.val == key:
                    pre.next = curr.next
                    return
                
                pre = curr
                curr = curr.next
        
class MyHashSet:

    def __init__(self):
        self.lst = [Bucket() for _ in range(769)]
    
    def _hash(self, key):
        return key % 769

    def add(self, key: int) -> None:
        idx = self._hash(key)
        self.lst[idx].addNode(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        self.lst[idx].removeNode(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return self.lst[idx].nodeExists(key)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
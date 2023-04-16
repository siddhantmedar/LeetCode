class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.pre = None
        

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1001)
        self.tail = Node(-1001)
        self.size = 0
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, index: int) -> int:
        if index < self.size:
            i = 0
            tmp = self.head.next

            while i!=index:
                i+=1
                tmp = tmp.next        

            if i==index:
                return tmp.val

        return -1
    
    
    def addAtHead(self, val: int) -> None:
        node = Node(val)
        ref = self.head.next
        
        self.head.next = node
        node.pre = self.head
        ref.pre = node
        node.next = ref
        
        self.size+=1
        
    def addAtTail(self, val: int) -> None:
        node = Node(val)
        
        ref = self.tail.pre
        ref.next = node
        node.pre = ref
        node.next = self.tail
        self.tail.pre = node
        
        self.size+=1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.size:
            i = 0
            node = Node(val)
            tmp = self.head.next

            while i!=index:
                i+=1
                tmp = tmp.next

            pre = tmp.pre
            pre.next = node
            node.pre = pre
            tmp.pre = node
            node.next = tmp
            
            self.size+=1
            

    def deleteAtIndex(self, index: int) -> None:
        if index < self.size:
            i = 0
            tmp = self.head.next

            while i!=index:
                i+=1
                tmp = tmp.next

            pre = tmp.pre
            nxt = tmp.next

            pre.next = nxt
            nxt.pre = pre
            
            self.size-=1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
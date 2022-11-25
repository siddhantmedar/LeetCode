class Node:
    def __init__(self,s,e):
        self.start = s
        self.end = e
        self.left = None
        self.right = None
        
    def insert(self,node):
        if node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            else:
                return self.left.insert(node)
        
        elif self.end <= node.start:
            if not self.right:
                self.right = node
                return True
            else:
                return self.right.insert(node)
        else:
            return False
        
class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start,end)
            return True
            
        return self.root.insert(Node(start,end))

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        clone = {None:None}
    
        tmp = head
        
        while tmp:
            clone[tmp] = clone.get(tmp, Node(tmp.val))
            
            tmp = tmp.next
            
        tmp = head
        
        while tmp:
            clone[tmp].next = clone[tmp.next]
            clone[tmp].random = clone[tmp.random]
            
            tmp = tmp.next
            
        return clone[head]
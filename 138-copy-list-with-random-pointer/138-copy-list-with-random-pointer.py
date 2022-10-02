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
        tmp = head
        
        while tmp:
            ref = tmp.next
            dummy = Node(tmp.val)
            tmp.next = dummy
            dummy.next = ref
            
            tmp = tmp.next.next
            
        tmp = head
        
        while tmp:
            tmp.next.random = tmp.random.next if tmp.random else None
            tmp = tmp.next.next
            
        dummy = ListNode(-1001)
        ptr = dummy
        
        tmp = head
        
        while tmp:
            ptr.next = tmp.next
            ptr = ptr.next
            
            tmp.next = tmp.next.next
            
            tmp = tmp.next
            
        return dummy.next
            
        
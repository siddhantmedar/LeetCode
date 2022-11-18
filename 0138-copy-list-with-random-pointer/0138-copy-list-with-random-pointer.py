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
            node = Node(tmp.val)
            tmp.next = node
            node.next = ref
            tmp = tmp.next.next
        
        tmp = head
        
        while tmp:
            tmp.next.random = tmp.random.next if tmp.random else None
            tmp = tmp.next.next
            
        dummy = ListNode(-1)
        tmp = dummy
        
        while head:
            ref = head.next.next
            
            tmp.next = head.next
            tmp = tmp.next
            
            head.next = ref
            
            head = head.next
            
        return dummy.next
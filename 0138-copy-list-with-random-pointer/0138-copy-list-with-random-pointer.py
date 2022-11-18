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
        mp = {None:None}
        
        tmp = head
        
        while tmp:
            if tmp not in mp:
                mp[tmp] = Node(tmp.val)
                
            tmp = tmp.next 
        
        tmp = head
        
        while tmp:
            mp[tmp].next = mp[tmp.next]
            mp[tmp].random = mp[tmp.random]
            
            tmp = tmp.next
            
        
        return mp[head]
            
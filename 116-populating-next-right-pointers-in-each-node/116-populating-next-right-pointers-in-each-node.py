"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        q = deque([root,"#"])
        
        while q:
            n = len(q)
            
            for k in range(n):
                if q[0] == "#":
                    q.popleft()
                    continue
                
                node = q.popleft()
                
                node.next = q[0] if q[0] != "#" else None
                
                if node.left:
                    q.append(node.left)
                   
                if node.right:
                    q.append(node.right)
                   
            if q:
                q.append("#")
                   
        return root
        
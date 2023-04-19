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
        def solve(root):
            if not root:
                return
            
            q = deque([root,"#"])
            
            while q:
                n = len(q)
                
                for _ in range(n):
                    node = q.popleft()
                    if node=="#":
                        continue
                    
                    if q and q[0] != "#":
                        node.next = q[0]
                    
                    if node.left:
                        q.append(node.left)
                        
                    if node.right:
                        q.append(node.right)
                
                if q:
                    q.append("#")
                print(q)
            return root
        
        solve(root)
        
        return root
                            
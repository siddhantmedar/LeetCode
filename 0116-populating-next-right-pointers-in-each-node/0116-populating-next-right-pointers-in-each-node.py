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
        def dfs(root,level):
            if not root:
                return
            
            mp[level].append(root)
            
            dfs(root.left,level+1)
            dfs(root.right,level+1)
        
        if not root:
            return root
        
        mp = defaultdict(list)
        
        dfs(root,1)
        
        for _,v in mp.items():
            for i in range(len(v)-1):
                v[i].next = v[i+1]
                
        return root
        
                
        
        
        
#         q = deque([root,"#"])
        
#         while q:
#             n = len(q)
            
#             for _ in range(n):
#                 node = q.popleft()
                
#                 if node == "#":
#                     continue
                
#                 if q and q[0] != "#":
#                     node.next = q[0]
                    
#                 if node.left:
#                     q.append(node.left)
                    
#                 if node.right:
#                     q.append(node.right)
                
#             if q:
#                 q.append("#")
        
#         return root
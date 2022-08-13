"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        def DFS(root):
            def solveDFS(root):
                if not root:
                    return root

                mp[root] = Node(root.val)

                mp[root].children = [solveDFS(c) for c in root.children]

                return mp[root]

            mp = {}

            return solveDFS(root)
        
        # return DFS()
    
        def solveBFS(root):
            if not root:
                return root
            
            mp = {root: Node(root.val)}
            
            q = deque([root])
            
            while q:
                n = len(q)
                
                for i in range(n):
                    node = q.popleft()
                        
                    for c in node.children:
                        mp[c] = Node(c.val)
                        mp[node].children.append(mp[c])
                        q.append(c)

            return mp[root]

        return solveBFS(root)
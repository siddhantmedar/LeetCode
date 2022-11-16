"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        def dfs(root):
            if not root:
                return
            
            if root not in mp:
                mp[root] = Node(root.val)
                
            visited.add(root)
            
            for nei in root.children:
                if nei not in mp:
                    mp[nei] = Node(nei.val)
                    
                mp[root].children.append(mp[nei])
                
                if nei not in visited:
                    dfs(nei)
            
        
        if not root:
            return None
        
        mp = {None:None}
        visited = set()
        
        dfs(root)
        
        return mp[root]
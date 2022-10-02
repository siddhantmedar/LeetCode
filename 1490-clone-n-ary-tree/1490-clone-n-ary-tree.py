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
            
            mp[root] = mp.get(root, Node(root.val))
            
            for c in root.children:
                if c:
                    mp[c] = mp.get(c, Node(c.val))
                    
                mp[root].children.append(mp[c])
                
                dfs(c)
                
            
        mp = {None:None}
        
        dfs(root)
        
        return mp[root]
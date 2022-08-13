"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        def solve(root):
            if not root:
                return root
            
            mp[root] = Node(root.val)
            
            mp[root].children = [solve(c) for c in root.children]
            
            return mp[root]
        
        mp = {}
        
        return solve(root)
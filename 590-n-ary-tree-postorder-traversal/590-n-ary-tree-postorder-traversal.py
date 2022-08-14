"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def solve(root):
            if not root:
                return

            for c in root.children:
                solve(c)
                
            res.append(root.val)
                
        res = []
        
        solve(root)
        
        return res
        
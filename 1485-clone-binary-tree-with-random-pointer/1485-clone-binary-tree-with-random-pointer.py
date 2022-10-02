# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        def dfs(root):
            if not root:
                return
            
            mp[root] = mp.get(root, NodeCopy(root.val))
            
            dfs(root.left)    
            dfs(root.right)
            
            
        def link(root):
            if not root:
                return
            
            mp[root].left = mp[root.left if root else None]
            mp[root].right = mp[root.right if root else None]    
            mp[root].random = mp[root.random if root else None]
            
            link(root.left)
            link(root.right)
            
        if not root:
            return None
        
        mp = {None:None}
        
        dfs(root)
        link(root)
        
        return mp[root]
# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        def bfs(root):
            if not root:
                return
            
            q = deque([root])
            mp[root] = NodeCopy(root.val)
            
            while q:
                n = len(q)
                
                for k in range(n):
                    node = q.popleft()
                    
                    if node.left:
                        mp[node.left] = NodeCopy(node.left.val)
                        q.append(node.left)
                    if node.right:
                        mp[node.right] = NodeCopy(node.right.val)
                        q.append(node.right)
        
        def link(root):
            if not root:
                return None
            
            q = deque([root])
            
            while q:
                n = len(q)
                
                for k in range(n):
                    node = q.popleft()
                    
                    mp[node].left = mp[node.left]
                    mp[node].right = mp[node.right]
                    mp[node].random = mp[node.random]
            
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
        if not root:
            return None
        
        mp = {None:None}
        
        bfs(root)
        link(root)
        
        return mp[root]
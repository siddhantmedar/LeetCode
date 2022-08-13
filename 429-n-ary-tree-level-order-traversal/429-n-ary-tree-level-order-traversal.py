"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def BFS():
            if not root:
                return []

            res = []

            q = deque([root])

            while q:
                n = len(q)
                tmp = []

                for i in range(n):
                    node = q.popleft()
                    tmp.append(node.val)

                    for c in node.children:
                        q.append(c)

                res.append(tmp)

            return res
        
        # return BFS()
    
        def DFS(root):
            mp = {i:[] for i in range(1, 1001)}
            
            def dfs(root, level):
                if not root:
                    return
                
                mp[level].append(root.val)
                
                for c in root.children:
                    dfs(c,level+1)
                
            dfs(root, 1)
            
            return [v for k,v in mp.items() if v]
                
        
        return DFS(root)
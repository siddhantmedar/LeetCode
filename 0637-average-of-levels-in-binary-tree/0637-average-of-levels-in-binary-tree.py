# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        mp = defaultdict(list)
        
        def bfs(root):
            if not root:
                return []
            
            res = []
            
            q = deque([root])
            
            while q:
                n = len(q)
                tmp = []
                for _ in range(n):
                    node = q.popleft()
                    tmp.append(node.val)

                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.right)
                    
                res.append(sum(tmp)/len(tmp))
            
            return res
        
        
        def dfs(root, l):
            if not root:
                return
            
            mp[l].append(root.val)
            
            dfs(root.left, l+1)
            dfs(root.right, l+1)
            
        return bfs(root)
        
        # return [sum(v)/len(v) for _,v in mp.items()]
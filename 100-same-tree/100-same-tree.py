# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p,q):
            if not p and not q:
                return True

            if (p and not q) or (q and not p):
                return False

            return p.val == q.val and dfs(p.left, q.left) and dfs(p.right, q.right)
    
        def bfs(p,q):
            q = deque([(p,q)])
            
            while q:
                node1, node2 = q.popleft()
                
                if (node1 and not node2) or (node2 and not node1) or\
                    (node1 and node2 and (node1.val != node2.val)):
                    return False
                
                if (node1 and node1.left) or (node2 and node2.left):
                    q.append((node1.left if node1 else None, node2.left if node2 else None))
                
                if (node1 and node1.right) or (node2 and node2.right):
                    q.append((node1.right if node1 else None, node2.right if node2 else None))
            
            return True
        
        return bfs(p,q)
                
                
                
                
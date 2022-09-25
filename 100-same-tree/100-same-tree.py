# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        queue = deque([(root1,root2)])
        
        while queue:
            n = len(queue)
            
            for k in range(n):
                p,q = queue.popleft()
                
                if not p and not q:
                    return True
        
                if (not p and q) or (p and not q) or (p.val != q.val):
                    return False
                
                if p.left or q.left:
                    queue.append([p.left if p.left else None, q.left if q.left else None])
                    
                if p.right or q.right:
                    queue.append([p.right if p.right else None, q.right if q.right else None])
                    
        return True
                    
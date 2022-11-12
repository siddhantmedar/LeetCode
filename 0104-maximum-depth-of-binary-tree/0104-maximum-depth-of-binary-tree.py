# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if not root:
                return 0
            
            q = deque([root])
            
            cnt = 0
            
            while q:
                n = len(q)
                cnt+=1
                for k in range(n):
                    node = q.popleft()
                    
                    if node.left:
                        q.append(node.left)
                        
                    if node.right:
                        q.append(node.right)
                        
            return cnt
        
        return solve(root)
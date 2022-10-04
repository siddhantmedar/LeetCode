# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        result = 0
        
        q = deque([(1,root)])
        
        while q:
            n = len(q)
            
            result = max(result, q[-1][0]-q[0][0]+1)
            
            for k in range(n):
                idx, node = q.popleft()
                
                if node.left:
                    q.append((2*idx, node.left))
                    
                if node.right:
                    q.append((2*idx+1, node.right))
                    
        return result
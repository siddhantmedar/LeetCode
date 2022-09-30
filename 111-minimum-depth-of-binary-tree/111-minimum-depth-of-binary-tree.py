# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level = 0
        
        q = deque([root])
        
        while q:
            n = len(q)
            level+=1
            
            for k in range(n):
                node = q.popleft()
                
                if not node.left and not node.right:
                    return level
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
        return level
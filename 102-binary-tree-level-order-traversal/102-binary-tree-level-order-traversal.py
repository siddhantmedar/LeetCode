# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        
        q = deque([root])
        
        while q:
            n = len(q)
            lst = []
            
            for k in range(n):
                node = q.popleft()
                lst.append(node.val)
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
            result.append(lst)
            
        return result
        
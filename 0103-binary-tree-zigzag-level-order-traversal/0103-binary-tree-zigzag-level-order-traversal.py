# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        
        q = deque([root])
        bit = True
        
        while q:
            n = len(q)
            tmp = deque()
        
            for k in range(n):
                node = q.popleft()
                
                if bit:
                    tmp.append(node.val)
                else:
                    tmp.appendleft(node.val)
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
            result.append(tmp)
            bit = not bit
            
        return result
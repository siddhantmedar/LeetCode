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
        
        result = deque()
        
        flag = 1
        
        q = deque([root])
        
        while q:
            n = len(q)
            tmp = []
            
            for k in range(n):
                node = q.popleft()
                tmp.append(node.val)
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
            
            if flag:
                result.append(tmp)
    
            else:
                result.append(tmp[::-1])
            
            flag = not flag
            
        return result
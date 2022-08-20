# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, root)])
        
        while q:
            n = len(q)
            
            for i in range(n):
                node1, node2 = q.popleft()
                
                if (node1 and not node2) or (node2 and not node1):
                    return False
                
                if node1.val != node2.val:
                    return False
                
                if node1.left or node2.right:
                    q.append((node1.left if node1 else None, node2.right if node2 else None))
                if node1.right or node2.left:
                    q.append((node1.right if node1 else None, node2.left if node2 else None))
                             
        return True
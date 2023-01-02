# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = [root.val]
        
        q = deque([root])
        
        while q:
            tmp = []
            
            for node in q:
                if node.left:
                    tmp.append(node.left)
                    
                if node.right:
                    tmp.append(node.right)
                    
            q = tmp
            
            if q:
                res.append(q[-1].val)
            
        return res
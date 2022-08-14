# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def solve(root):
            if not root:
                return root
            
            if not root.left and not root.right:
                tmp.append(root.val)
                return None
                    
            root.left = solve(root.left)
            root.right = solve(root.right)
            
            return root
        
        res = []
        
        while root:
            tmp = []
            root = solve(root)
            res.append(tmp)
            
        return res
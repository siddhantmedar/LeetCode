# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaf(root,res):
            if not root:
                return
            
            if not root.left and not root.right:
                res.append(root.val)
                
            getLeaf(root.left,res)
            getLeaf(root.right,res)
            
            
        res1, res2 = [], []
        
        getLeaf(root1, res1)
        getLeaf(root2, res2)
        
        return res1 == res2
            
        
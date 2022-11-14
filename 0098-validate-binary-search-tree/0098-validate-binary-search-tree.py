# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            
        def check(lst):
            for i in range(len(lst)-1):
                if lst[i] >= lst[i+1]:
                    return False
                
            return True
            
        res = []
        
        inorder(root)
        
        return check(res)
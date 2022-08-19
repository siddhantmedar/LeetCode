# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first, last, mid, pre = None, None, None, None
        
        def inorder(root):
            nonlocal first, last, mid, pre
            
            if not root:
                return
            
            inorder(root.left)
            
            if pre and pre.val > root.val:
                if not first:
                    first = pre
                    mid = root
                else:
                    last = root
            
            pre = root
            inorder(root.right)
            
        inorder(root)
        
        if first and mid and not last:
            first.val, mid.val = mid.val, first.val
            
        elif first and mid and last:
            first.val, last.val = last.val, first.val
        
        return root
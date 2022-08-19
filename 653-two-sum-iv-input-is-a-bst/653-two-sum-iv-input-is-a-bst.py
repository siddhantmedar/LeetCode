# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder(root):
            return inorder(root.left)+[root.val]+inorder(root.right) if root else []
        
        nums = inorder(root)
        
        st = set()
        
        for i, ele in enumerate(nums):
            if k-ele in st:
                return True
            
            st.add(ele)
            
        return False
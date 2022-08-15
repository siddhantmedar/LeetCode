# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        st = [root]
        res = []
        
        while st:
            node = st.pop()
            res.append(node.val)
            
            if node.right:
                st.append(node.right)
                
            if node.left:
                st.append(node.left)
                
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mp = defaultdict()
        
        for i, ele in enumerate(inorder):
            mp[ele] = i
            
        def solve(sp, ep, si, ei):
            if sp > ep or si > ei:
                return None
            
            root = TreeNode(postorder[ep])
            idx = mp[postorder[ep]]
            count = idx-si
            
            root.left = solve(sp, sp+count-1, si, idx-1) 
            root.right = solve(sp+count, ep-1, idx+1, ei)
            
            return root
        
        return solve(0, len(postorder)-1, 0, len(inorder)-1)
        
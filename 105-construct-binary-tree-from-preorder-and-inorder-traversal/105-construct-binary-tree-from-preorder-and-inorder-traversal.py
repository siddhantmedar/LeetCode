# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def getIdx(ele):
            for i,x in enumerate(inorder):
                if ele == x:
                    return i
            
        def solve(sp, ep, si, ei):
            if sp > ep or si > ei:
                return None
            
            root = TreeNode(preorder[sp])
            
            idx = getIdx(preorder[sp])
            
            root.left = solve(sp+1,sp+(idx-si),si,idx-1)
        
            root.right = solve(sp+(idx-si)+1,ep,idx+1, ei)
            
            return root
        
        
        return solve(0,len(preorder)-1,0,len(inorder)-1)
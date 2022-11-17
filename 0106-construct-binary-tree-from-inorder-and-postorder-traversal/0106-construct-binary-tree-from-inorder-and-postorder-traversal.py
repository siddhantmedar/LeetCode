# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def solve(ps,pe,iss,ie):
            if ps>pe or iss>ie:
                return None
            
            root = TreeNode(postorder[pe])
            idx = find[postorder[pe]]
            
            root.left = solve(ps,ps+(idx-iss)-1,iss,idx-1)
            root.right = solve(ps+(idx-iss),pe-1,idx+1,ie)
            
            return root
        
        find = {ele:i for i,ele in enumerate(inorder)}
        
        return solve(0,len(postorder)-1,0,len(inorder)-1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:       
        def solve(ps,pe,iss,ie):
            if ps>pe or iss>ie:
                return None
            
            root = TreeNode(preorder[ps])
            idx = find[preorder[ps]]
            
            root.left = solve(ps+1,ps+(idx-iss),iss,idx-1)
            root.right = solve(ps+(idx-iss)+1,pe,idx+1,ie)
            
            return root
        
        find = {ele:i for i,ele in enumerate(inorder)}
        
        return solve(0,len(preorder)-1,0,len(inorder)-1)
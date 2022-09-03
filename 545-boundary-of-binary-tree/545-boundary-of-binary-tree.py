# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def isLeaf(root):
            return not root.left and not root.right
    
        def dfs(root):
            if not root:
                return
                
            dfs(root.left)
            
            if not root.left and not root.right:
                res.append(root.val)
            
            dfs(root.right)
                
        res = []
        
        if root and not isLeaf(root):
            res.append(root.val)
        
        tmp = root.left
        
        while tmp:
            if not isLeaf(tmp):
                res.append(tmp.val)
                
            tmp = tmp.left if tmp.left else tmp.right
            
        dfs(root)
        
        tmp = root.right
        
        rev = []
        
        while tmp:
            if not isLeaf(tmp):
                rev.append(tmp.val)
                
            tmp = tmp.right if tmp.right else tmp.left
        
        return res+rev[::-1]
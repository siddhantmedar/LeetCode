# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def getPath(root, target, path):
            nonlocal found
            
            if not root:
                return
            
            path.append(root)
            
            if root == target:
                found = True
                return
            
            getPath(root.left, target, path)
            
            if found:
                return
            
            getPath(root.right, target, path)
            
            if found:
                return
            
            path.pop()
            
        path1, path2 = [], []
        
        found = False
        getPath(root, p, path1)
        
        found = False
        getPath(root, q, path2)
        
        result = None
        
        for i in range(min(len(path1), len(path2))):
            if path1[i] == path2[i]:
                result = path1[i]
                
        return result
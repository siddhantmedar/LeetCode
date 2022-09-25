# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, target, path):
            if not root:
                return False
            
            mp[root.val] = root
            
            path.append(root.val)
            
            if root.val == target.val:
                return True
            
            if dfs(root.left, target, path) or dfs(root.right, target, path):
                return True
                
            path.remove(root.val)
            
            return False
            
        p1, p2 = [], []
        mp = defaultdict()
        
        dfs(root, p, p1)
        dfs(root, q, p2)
        
        p2 = set(p2)
        
        result = None
        
        for node in p1:
            if node in p2:
                result = node
                
        return mp[result]
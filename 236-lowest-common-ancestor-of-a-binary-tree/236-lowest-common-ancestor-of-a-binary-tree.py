# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, path, node):
            if not root:
                return False
            
            mp[root.val] = root
            
            path.append(root.val)
            
            if root == node:
                return True
            
            left = dfs(root.left, path, node)
            right = dfs(root.right, path, node)
            
            if left or right:
                return True
            
            path.remove(root.val)
            
            return False
        
        mp = defaultdict()
        
        path1, path2 = [],[]
        
        dfs(root, path1, p)
        dfs(root, path2, q)
        
        # print(path1, path2)
    
        tmp = set(path2)
        
        result = None
        
        for ele in path1:
            if ele in tmp:
                result = ele
                
        return mp[result]
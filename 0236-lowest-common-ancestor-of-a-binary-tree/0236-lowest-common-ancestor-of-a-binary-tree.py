# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root,target,lst):
            if not root:
                return False
            
            lst.append(root.val)
            mp[root.val] = root
            if root == target:
                return True
            
            if dfs(root.left,target,lst) or dfs(root.right,target,lst):
                return True
            
            lst.pop()
            
            return False
        
        
        lst1,lst2 = [],[]
        mp = {}
        
        dfs(root,p,lst1)
        dfs(root,q,lst2)
        
        result = None
        
        l1,l2 = set(lst1), set(lst2)
        result = None
        
        if len(lst1) < len(lst2):
            for i in range(len(lst1)):
                if lst1[i] in l2:
                    result = lst1[i]
            
        else:
            for i in range(len(lst2)):
                if lst2[i] in l1:
                    result = lst2[i]
            
        return mp[result]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def buildParent(root, par=None):
            if not root:
                return
            
            if not root.left and not root.right:
                src.append(root)
            
            parent[root] = par
            
            buildParent(root.left, root)
            buildParent(root.right, root)
        
        def dfs(root, s, k):
            nonlocal count
            
            if not root:
                return
            
            visited.add(root)
            
            if k <= distance and (not root.left and not root.right) and root != s:
                count+=1
                return
            
            for c in [root.left, root.right, parent[root]]:
                if c and c not in visited:
                    if k < distance:
                        dfs(c, root, k+1)
        
        parent = {}
        src = []
        
        count  = 0
        buildParent(root)
        
        for node in src:
            visited = set()
            dfs(node, node, 0)
            
        return count//2
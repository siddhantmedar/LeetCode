# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root,level,idx):
            if not root:
                return
            
            mp[level].append(idx)
            
            dfs(root.left, level+1, 2*idx)
            dfs(root.right, level+1, 2*idx+1)
            
        mp = defaultdict(list)
        
        dfs(root,1,1)
        
        result = float("-inf")
        
        for k,v in mp.items():
            mx, mn = float("-inf"), float("inf")
            
            for ele in v:
                if ele > mx: mx = ele
                if ele < mn: mn = ele
            
            result = max(result, mx-mn+1)
            
        return result
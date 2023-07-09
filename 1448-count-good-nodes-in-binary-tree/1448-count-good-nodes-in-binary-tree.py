# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, mx):
            if not root:
                return 0
            
            cnt = 0
            
            if root.val >= mx:
                cnt+=1
                
            return cnt + dfs(root.left,max(mx,root.val)) + dfs(root.right, max(mx,root.val))
        
        return dfs(root,float("-inf"))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def solve1(root):
            if not root:
                return 0
            
            return max(solve(root.left), solve(root.right)) + 1
        
        def solve2(root):
            if not root:
                return 0
            
            level = 0
            
            q = deque([root])
            
            while q:
                n = len(q)
                level+=1
            
                for k in range(n):
                    node = q.popleft()
                    
                    if node.left:
                        q.append(node.left)
                        
                    if node.right:
                        q.append(node.right)
                        
            return level
                    
                    
                    
                    
        return solve2(root)
        
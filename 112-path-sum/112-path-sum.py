# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def solve(root, rem):
            if not root:
                return False
            
            if not root.left and not root.right:
                if rem-root.val == 0:
                    return True
            
                elif rem-root.val < 0:
                    return False
            
            return solve(root.left, rem-root.val) or solve(root.right, rem-root.val)
        
        return solve(root, targetSum)
        
        def solve2(root, rem):
            q = deque([(root, targetSum)])

            while q:
                n = len(q)

                for k in range(n):
                    node, rem = q.popleft()

                    if not node.left and not node.right:
                        if rem-node.val == 0:
                            return True

                    if node.left:
                        q.append((node.left, rem-root.val))

                    if node.right:
                        q.append((node.right, rem-root.val))

            return False

        
        return solve2(root, targetSum)
        
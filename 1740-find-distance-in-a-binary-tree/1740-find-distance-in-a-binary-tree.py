# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        def lca(root):
            if not root:
                return root
            
            if root.val == p or root.val == q:
                return root
            
            left = lca(root.left)
            right = lca(root.right)
            
            if left and right:
                return root
            
            return left or right
        
        result = 0
        level = 0
        
        res = lca(root)
        
        qq = deque([res])
        
        while qq:
            n = len(qq)
            
            for _ in range(n):
                node = qq.popleft()
                if node.val == p or node.val == q:
                    # print(node.val, level)
                    result+=level
                    
                if node.left:
                    qq.append(node.left)
                    
                if node.right:
                    qq.append(node.right)
            
            # print([x.val for x in qq],end="\n")
            level+=1    
        
        return result
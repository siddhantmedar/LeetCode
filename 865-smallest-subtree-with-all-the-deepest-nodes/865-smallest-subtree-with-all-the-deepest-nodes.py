# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def bfs(root):           
            q = deque([root])
            
            while q:
                n = len(q)
                tmp = []
                for i in range(n):
                    node = q.popleft()
                    tmp.append(node)
                    
                    if node.left:
                        q.append(node.left)
                        
                    if node.right:
                        q.append(node.right)
                        
                lst = tmp
            
            return lst
        
        def lca(root):
            if not root or (root in st):
                return root

            left = lca(root.left)
            right = lca(root.right)

            if left and right:
                return root

            return left or right

        st = set(bfs(root))
        return lca(root)
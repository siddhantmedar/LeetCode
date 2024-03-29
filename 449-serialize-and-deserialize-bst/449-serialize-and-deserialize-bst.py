# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        
        def dfs(root):
            nonlocal lst
            
            if not root:
                lst+="#"
                lst+=","
                return
            
            lst+=str(root.val)
            lst+=","
            
            dfs(root.left)
            dfs(root.right)
            
        lst = ""
        
        dfs(root)
        
        return lst[:-1]
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        def dfs():
            node = q.popleft()
            
            if node != "#":
                root = TreeNode(node)

                root.left = dfs()
                root.right = dfs()
            
            elif node == "#":
                root = None
            
            return root
            
        q = deque(data.split(","))

        return dfs()
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
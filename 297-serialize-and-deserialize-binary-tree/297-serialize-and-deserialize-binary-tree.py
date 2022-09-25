# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
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
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
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
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
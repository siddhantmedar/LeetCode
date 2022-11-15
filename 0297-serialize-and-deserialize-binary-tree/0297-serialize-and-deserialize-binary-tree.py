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
            nonlocal result
            
            if not root:
                result.append("#,")
                return
            
            result.append(str(root.val)+",")
            dfs(root.left)
            dfs(root.right)
        
        
        result = []
        dfs(root)
        print("".join(result)[:-1])
        return "".join(result)[:-1]
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs():
            if q[0] == "#":
                q.popleft()
                return None
            
            val = q.popleft()
            root = TreeNode(int(val))
            root.left = dfs()
            root.right = dfs()
            
            return root
        
        q = deque(data.split(','))
        
        return dfs()
    
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        def dfs(root):
            nonlocal s
            
            if not root:
                s+="#,"
                return
            
            s+=str(root.val)+","
            
            dfs(root.left)
            dfs(root.right)
            
        s = ""
        
        dfs(root)
        
        return "".join(s[:-1])
        
    def deserialize(self, data):
        q = deque(data.split(","))
        
        def dfs():
            if q[0] == "#":
                q.popleft()
                return None
            
            val = q.popleft()
            
            root = TreeNode(val)
            
            root.left = dfs()
            root.right = dfs()
            
            return root
            
        return dfs()
            
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
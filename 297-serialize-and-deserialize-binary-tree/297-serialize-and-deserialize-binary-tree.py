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
        s = ""
        
        def solve(root):
            nonlocal s
            
            if not root:
                s+="#,"
                return
            
            s+=str(root.val)+","
            solve(root.left)
            solve(root.right)
            
        solve(root)
        print(s)
        print(s[:-1])
        return s[:-1]
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        lst = deque(data.split(","))
        
        def solve(lst):
            if lst[0] == "#":
                lst.popleft()
                return None
                
            root = TreeNode(int(lst.popleft()))
            
            root.left = solve(lst)
            root.right = solve(lst)
            
            return root
        
        return solve(lst)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
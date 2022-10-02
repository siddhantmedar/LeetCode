# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None
        
        mp = {None:None}
        
        st = [root]

        while st:
            node = st.pop()
            
            mp[node] = mp.get(node, NodeCopy(node.val))
            
            if node.left:
                st.append(node.left)
                
            if node.right:
                st.append(node.right)
                
        st = [root]
        
        while st:
            node = st.pop()
            
            mp[node].left = mp[node.left]
            mp[node].right = mp[node.right]
            mp[node].random = mp[node.random]
            
            if node.left:
                st.append(node.left)
                
            if node.right:
                st.append(node.right)
        
        return mp[root]
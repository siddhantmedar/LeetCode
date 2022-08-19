# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.st = []
        
        curr = root
        
        while curr:
            self.st.append(curr)
            curr = curr.left

    def next(self) -> int:
        node = self.st.pop()
        
        tmp = node.right
        
        while tmp:
            self.st.append(tmp)
            tmp = tmp.left
        
        return node.val

    def hasNext(self) -> bool:
        return len(self.st) != 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
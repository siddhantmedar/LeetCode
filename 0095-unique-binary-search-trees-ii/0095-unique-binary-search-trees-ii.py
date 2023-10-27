# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def solve(start,end):
            result = []
            
            if start > end:
                result.append(None)
                return result
            
            for i in range(start, end+1):
                # i becomes the root
                left = solve(start,i-1) # will have all combs of left sub tree
                right = solve(i+1,end) # will have all combs of right sub tree
            
                print(f"for node {i}, the left and right are {left} and {right}")
                for l in left:
                    for r in right:
                        print(l,r)
                        root = TreeNode(i,l,r)
                        result.append(root)

            return result


        return solve(1,n)
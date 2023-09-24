class Node:
    def __init__(self, val=""):
        self.val = val
        self.children = defaultdict()

class TrieNode:
    def __init__(self):
        self.root = Node()
        
    def insertWords(self, lst):
        for word in lst:
            node = self.root
            
            for c in word:
                if c not in node.children:
                    node.children[c] = Node(c)
                node = node.children[c]
                
            node.end = True
            
        return self.root  # Return the root node


class Solution:
    def longestWord(self, words: List[str]) -> str:
        def solve(root,s):
            nonlocal result,mx
            
            if len(s) >= mx:
                if len(s) > mx:
                    mx = len(s)
                    result = s
                if len(s) == mx:
                    mx = len(s)
                    result = min(s,result)
                
            print(s)
#             if len(result) >= len(s):
#                 if len(result) > len(s):
#                     print(result,s)
#                     result = s
            
#                 if len(result) == len(s):
#                     print("min of ", result,s,min(result,s))
#                     result = min(result,s)
            
            for child in root.children:
                if s+root.children[child].val in st:
                    solve(root.children[child], s+root.children[child].val)
            
        
        st = set(words)
        root = TrieNode().insertWords(words)
        result, mx = None, float("-inf")
        solve(root,"")
        
        print(result)
        
        return result
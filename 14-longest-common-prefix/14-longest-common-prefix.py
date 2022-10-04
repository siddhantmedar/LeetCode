class Trie:
    def __init__(self):
        self.children = dict()
        self.end = False
        
    @staticmethod
    def insertWords(lst):
        root = Trie()
        
        for word in lst:
            node = root
            
            for c in word:
                if c not in node.children:
                    node.children[c] = Trie()
                    
                node = node.children[c]
                
            node.end = True
        
        return root
        
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = Trie.insertWords(strs)
        
        node = root
        
        result = ""
        
        while len(node.children) == 1 and not node.end:
            nxt = None
            for k,v in node.children.items():
                result+=k
                nxt = k
                
            node = node.children[nxt]
            
        return result
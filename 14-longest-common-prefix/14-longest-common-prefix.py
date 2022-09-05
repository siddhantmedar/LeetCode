class Trie:
    def __init__(self, c=""):
        self.children = {}
        self.isEnd = False
        self.c = c
        
    @staticmethod
    def insertWords(strs):
        root = Trie()
        
        for word in strs:
            node = root
            
            for c in word:
                if c not in node.children:
                    node.children[c] = Trie(c)
                node = node.children[c]
            
            node.isEnd = True
            
        return root
            
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""
        
        root = Trie.insertWords(strs)
        
        res = ""
        
        node = root
        
        while len(node.children) == 1 and not node.isEnd:
            ch = None
            
            for k,v in node.children.items():
                res+=k
                ch = k
            
            node = node.children[ch]
        
        return res
class TrieNode:
    def __init__(self):
        self.val = None
        self.children = {}
        self.end = False

    @staticmethod
    def insertWords(words):
        root = TrieNode()
        
        for word in words:
            node = root
            
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                    
                node = node.children[c]
                node.val = c
            
            node.end = True
        
        return root
    

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        node = TrieNode().insertWords(strs)
        
        result = ""
        
        while len(node.children) == 1 and not node.end:
            key = None
            
            for k,v in node.children.items():
                key = k
            
            result+=key
            node = node.children[key]
            
        return result
            
        
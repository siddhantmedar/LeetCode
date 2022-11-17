class TrieNode:
    def __init__(self):
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
                
            node.end = True
            
        return root
    
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        root = TrieNode.insertWords(words)
        
        result = []
        
        for i in range(len(text)):
            node = root
            for j in range(i,len(text)):
                if text[j] not in node.children:
                    break
                
                node = node.children[text[j]]
                
                if node.end:
                    result.append([i,j])
                    
        return result
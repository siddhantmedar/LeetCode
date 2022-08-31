class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.root = self
        
    def insert(self, word: str) -> None:
        node = self.root
        
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
        
        node.isEnd = True
        
    def search(self, word: str) -> bool:
        node = self.root
        
        for c in word:
            if c not in node.children:
                return False
            else:
                node = node.children[c]
        
        return node.isEnd
    
    def startsWith(self, word: str) -> bool:
        node = self.root
        
        for c in word:
            if c not in node.children:
                return False
            else:
                node = node.children[c]
        
        return True
    
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
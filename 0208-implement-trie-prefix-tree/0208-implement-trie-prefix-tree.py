class Node:
    def __init__(self,val=None):
        self.val = val
        self.childrens = {}
        self.end = False
        
class Trie:

    def __init__(self):
        self.root = Node()
            
    def insert(self, word: str) -> None:
        node = self.root
        
        for c in word:
            if c not in node.childrens:
                node.childrens[c] = Node(c)
                
            node = node.childrens[c]
        
        node.end = True
        
    def search(self, word: str) -> bool:
        node = self.root
        
        for c in word:
            if c not in node.childrens:
                return False        
            node = node.childrens[c]
        
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for c in prefix:
            if c not in node.childrens:
                return False        
            node = node.childrens[c]
        
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
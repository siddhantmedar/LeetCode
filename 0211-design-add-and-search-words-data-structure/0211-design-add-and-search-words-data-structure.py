class Node:
    def __init__(self,val=None):
        self.val = val
        self.children = {}
        self.end = False
        
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
            
        node.end = True

    def search(self, word: str) -> bool:
        def solve(i,root):
            if i==len(word):
                return root.end
            
            if word[i] != ".":
                if word[i] in root.children:
                    return solve(i+1,root.children[word[i]])
                else:
                    return False
            else:
                return any(solve(i+1,root.children[child]) for child in root.children)
                     
            
        
        return solve(0,self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
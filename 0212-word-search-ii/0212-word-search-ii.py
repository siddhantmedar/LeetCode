class Node:
    def __init__(self,val=None):
        self.val = val
        self.children = {}
        self.end = False
        self.word = None
        
class Trie:
    def __init__(self):
        self.root = Node()

    def insertWords(self,lst):
        for word in lst:
            node = self.root
            for c in word:
                if c not in node.children:
                    node.children[c] = Node(c)

                node = node.children[c]
            
            node.end = True
            node.word = word
        
        return self.root
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(i,j,root,s):
            nonlocal result
            
            if (i,j) in visited: 
                return
            
            visited.add((i,j))
            
            root = root.children[board[i][j]]
            
            if root.end == True and root.word in words and root.word not in result:
                result.append(root.word)
            
            for dx,dy in directions:
                dx+=i
                dy+=j
                
                if 0<=dx<m and 0<=dy<n and board[dx][dy] in root.children and (dx,dy) not in visited:
                    dfs(dx,dy,root,s+board[dx][dy])
            
            visited.remove((i,j))
        
        
        m,n = len(board), len(board[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        root = Trie().insertWords(words)
        words = set(words)
        
        result = []
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in root.children:
                    visited = set()
                    dfs(i,j,root,"")
        
        return result
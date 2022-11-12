class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def toposort():
            q = deque([k for k,v in indegree.items() if v == 0])
            output = ""
            
            while q:
                node = q.popleft()
                output+=node
                
                for nei in graph[node]:
                    indegree[nei]-=1
                    
                    if indegree[nei] == 0:
                        q.append(nei)
            
            return output if len(indegree) == len(output) else ""
        
        graph = defaultdict(set)
        visited = set()
        rec = set()
        st = []
        
        indegree = {c:0 for word in words for c in word}
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            mn = min(len(w1), len(w2))
            
            if len(w1) > len(w2) and w1[:mn] == w2[:mn]:
                return ""
            
            for i, (c1, c2) in enumerate(zip(w1, w2)):
                if c1 == c2:
                    continue
                    
                else:
                    if c2 not in graph[c1]:
                        indegree[c2]+=1
                    
                    graph[c1].add(c2)
                    
                    break
        
        return toposort()
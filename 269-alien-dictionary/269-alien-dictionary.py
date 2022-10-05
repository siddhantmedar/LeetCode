class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def toposort():
            q = deque([k for k,v in indegree.items() if v == 0])
            
            result = ""
            
            while q:
                n = len(q)
                
                for k in range(n):
                    node = q.popleft()
                    result+=node
                    
                    for nei in graph[node]:
                        indegree[nei]-=1
                        
                        if indegree[nei] == 0:
                            q.append(nei)
                            
            return result if len(result) == len(indegree) else ""
            
        graph = defaultdict(set)
        indegree = {c:0 for word in words for c in word}
            
        for i in range(len(words)-1):
            x,y = words[i], words[i+1]
            
            mn = min(len(x), len(y))
            
            if len(x) > len(y) and x[:mn] == y[:mn]:
                return ""
            
            for i in range(mn):
                if x[i] != y[i]:
                    
                    if y[i] not in graph[x[i]]:
                        indegree[y[i]] = 1+indegree.get(y[i],0)
                        # indegree[x[i]] = indegree.get(x[i],0)
                    
                    graph[x[i]].add(y[i])
                    
                    break
        
        return toposort()
            
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def toposort():
            result = []
            q = deque([k for k,v in indegree.items() if v == 0])
            
            while q:
                node = q.popleft()
                result.append(node)
                
                if node in graph:
                    for nei in graph[node]:
                        indegree[nei]-=1

                        if indegree[nei] == 0:
                            q.append(nei)
            
            return result if len(result) == len(indegree) else []
                
        graph = defaultdict(set)
        indegree = {c:0 for word in words for c in word}
        
        for i in range(len(words)-1):
            x,y = words[i], words[i+1]
            
            l = min(len(x), len(y))
            
            if (len(x) > len(y) and y[:l] == x[:l]):
                return ""
            
            for j in range(l):
                w1 = x[j]
                w2 = y[j]
                
                if w1 != w2:
                    if w2 not in graph[w1]:
                        indegree[w2] = 1+indegree.get(w2, 0)
                    
                    graph[w1].add(w2)
                    
                    break
        
        result = toposort()

        return "".join(result)
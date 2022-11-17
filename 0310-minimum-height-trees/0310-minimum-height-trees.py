class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [x for x in range(n)]
        
        graph = defaultdict(set)
        
        for u,v in edges:
            graph[v].add(u)
            graph[u].add(v)
            
        rem = len(graph)
        
        q = deque([k for k,v in graph.items() if len(v)==1])
        
        while rem > 2:
            n = len(q)
            
            for _ in range(n):
                node = q.popleft()
                rem-=1
                
                tmp = None
                
                tmp = [x for x in graph[node]][0]
                del graph[node]
                
                graph[tmp].remove(node)
                
                if len(graph[tmp]) == 1:
                    q.append(tmp)
            
        return [x for x in q]
            
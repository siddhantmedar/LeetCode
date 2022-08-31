class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for u,v,w in times:
            graph[u].append((v,w))
            
        dist = {x:float("inf") for x in range(1, n+1)}
        visited = set()
        
        dist[k] = 0
        
        visited.add(k)
        q = [(0,k)]
        
        heapq.heapify(q)
        
        while q:
            cost, node = heapq.heappop(q)
            
            for nei, edge_cost in graph[node]:
                if dist[nei] > cost+edge_cost:
                    dist[nei] = cost+edge_cost
                    heapq.heappush(q,((dist[nei], nei)))
                    visited.add(nei)

        mx = max([v for _,v in dist.items()])
        
        return mx if mx != float("inf") else -1
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [0]*len(graph)
        
        for i in range(len(graph)):
            if colors[i] == 1  or colors[i] == -1:
                continue
            queue = []
            colors[i] = 1
            queue.append(i)
                        
            while len(queue) != 0:
                current = queue.pop(0)
                for j in graph[current]:
                    if colors[j] == 0:
                        colors[j] = -colors[current]
                        queue.append(j)
                    
                    if colors[current] == colors[j]:
                        return False
                    
        return True
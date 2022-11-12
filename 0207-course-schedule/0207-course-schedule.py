class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node):
            visited.add(node)
            rec.add(node)
            
            for nei in graph[node]:
                if nei not in visited:
                    if not dfs(nei):
                        return False
                    
                elif nei in rec:
                    return False
                    
            st.append(node)
            rec.remove(node)
            
            return True
            
        
        graph = defaultdict(list)
        
        for u,v in prerequisites:
            graph[v].append(u)
        
        visited = set()
        rec = set()
        st = []
        
        for i in range(n):
            if i not in visited:
                if not dfs(i):
                    return False
                
        print(st)
        
        return True
        
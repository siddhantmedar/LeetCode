class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        def solve(node):
            nonlocal result
            
            if node not in mp:
                return
            
            for nei in mp[node]:
                result.append(nei)
                
                solve(nei)
            
        
        mp = defaultdict(set)
        
        for child,parent in zip(pid,ppid):
            mp[parent].add(child)
            
        result = []
        
        solve(kill)
        
        return [kill]+result
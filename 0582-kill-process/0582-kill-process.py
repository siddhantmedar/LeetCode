class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        def buildPath(mp,node):
            if not mp[node]:
                return set([node])
            ans = set()
            ans.add(node)
            
            for ele in mp[node]:
                ans.update(buildPath(mp,ele))
            
            return ans
        
        
        mp = defaultdict(set)
        
        for i in range(len(pid)):
            if ppid[i] == 0:
                continue
            
            mp[ppid[i]].add(pid[i])
            
        result = list(buildPath(mp,kill))
        
        print(result)
        
        return result
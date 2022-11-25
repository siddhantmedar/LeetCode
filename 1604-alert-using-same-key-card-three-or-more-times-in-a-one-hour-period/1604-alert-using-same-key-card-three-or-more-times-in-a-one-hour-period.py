class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def convert(time):
            hr,mn = time[:2],time[3:]
            
            return int(hr)*60+int(mn)
        
        def check(lst):
            q = deque()
            for time in lst:
                while q and time-q[0] > 60:
                    q.popleft()
                
                q.append(time)
                if len(q) == 3:
                    return True
                
            return False
            
        
        keyTime = [convert(t) for t in keyTime]
        
        mp = defaultdict(list)
        
        for i in range(len(keyName)):
            mp[keyName[i]].append(keyTime[i])
            
        result = []
        
        for k,v in mp.items():
            v.sort()
            if check(v):
                result.append(k)
        
        result.sort()
        
        return result
    
    # O(no.of names*NlogN + no.of names*N + NlogN)
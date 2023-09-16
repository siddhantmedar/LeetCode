class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        mapping = defaultdict(list)
        
        lst = []
        
        for name,t,site in zip(username,timestamp,website):
            lst.append((name,t,site))
        
        lst.sort(key=lambda x:(x[0],x[1]))
        
        for name,t,site in lst:
            mapping[name].append(site)
                
        result = defaultdict()
        
        for k,v in mapping.items():
            pairs = Counter(set(combinations(v,3)))
            print(k,pairs)
            for p in pairs:
                result[tuple(p)]=1+result.get(tuple(p),0)
            
        mx = 0
        res = None
        print(result)
        for k,v in result.items():
            if v >= mx:
                if v > mx:
                    mx = v
                    res = k
                elif v == mx:
                    res = min(res, k)

        return res
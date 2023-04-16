class Solution:
    def areSentencesSimilar(self, s1: List[str], s2: List[str], similarPairs: List[List[str]]) -> bool:
        mp = defaultdict(set)
        
        for s,t in similarPairs:
                mp[s].add(t)
                mp[t].add(s)
            
        for i,(a,b) in enumerate(zip(s1,s2)):
            if a!=b and not (b in mp[a] and a in mp[b]):
                return False
            
        if len(s1)==len(s2):
            return True
        
        return False
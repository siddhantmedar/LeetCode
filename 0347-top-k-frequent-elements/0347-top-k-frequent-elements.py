class Solution:
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        mp = {}
        
        for ele in nums:
            mp[ele] = 1+mp.get(ele,0)
            
        size = max([v for k,v in mp.items()])
        
        container = [set() for _ in range(size+1)]
        
        for k,v in mp.items():
            container[v].add(k)
            
        result = []
        
        for i in range(len(container)-1,-1,-1):
            box = container[i]
            
            if box:
                for ele in box:
                    if len(result) == K:
                        break
                    
                    result.append(ele)
                    
        return result
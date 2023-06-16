class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = dict()
        
        for ele in nums:
            mp[ele] = 1 + mp.get(ele,0)
        
        container = [set() for _ in range(len(nums)+1)]
        
        for key,val in mp.items():
            container[val].add(key)
        
        i = len(container)-1
        
        res = []
        
        while i>=0:
            if k==0:
                break
            
            if container[i]:
                for ele in container[i]:
                    if k:
                        k-=1
                        res.append(ele)
            i-=1
        
        return res
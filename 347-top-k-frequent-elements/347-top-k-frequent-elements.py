class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict()
        
        for ele in nums:
            mp[ele] = 1+mp.get(ele, 0)
            
        mp = dict(sorted(mp.items(), key=lambda x:-x[1]))
        
        result = []
        
        for key,val in mp.items():
            result.append(key)
            k-=1
            
            if k == 0:
                break
                
        return result
        
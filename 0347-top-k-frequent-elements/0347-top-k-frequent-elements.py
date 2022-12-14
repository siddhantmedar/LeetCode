class Solution:
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        mp = dict()
        
        for ele in nums:
            mp[ele]=1+mp.get(ele,0)
        
        return [x[0] for x in sorted([(k,v) for k,v in mp.items()],key=lambda x:-x[1])[:K]]
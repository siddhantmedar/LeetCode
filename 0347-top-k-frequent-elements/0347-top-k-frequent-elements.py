class Solution:
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        mp = Counter(nums)
        
        lst = [(k,v) for k,v in mp.items()]
        
        lst = sorted(mp.items(), key=lambda x:-x[1])[:K]
        
        return [x[0] for x in lst]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = dict()
        
        for ele in nums:
            mp[ele] = 1 + mp.get(ele,0)
            
        res = sorted(mp.items(),key=lambda x:-x[1])
        print(res)
        return [x[0] for x in res][:k]
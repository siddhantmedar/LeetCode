class Solution:
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        mp = dict()
        
        for ele in nums:
            mp[ele]=1+mp.get(ele,0)
            
        print(mp)
        
        mp = dict(sorted(mp.items(),key=lambda x:-x[1]))
        
        print(mp)
        
        return [k for k,v in mp.items()][:K]
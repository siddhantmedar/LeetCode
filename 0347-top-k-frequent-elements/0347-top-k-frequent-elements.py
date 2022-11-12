class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        
        for ele in nums:
            mp[ele] = 1+mp.get(ele,0)
            
        lst = sorted(mp.items(),key=lambda x:-x[1])
        
        return [x[0] for x in lst[:k]]
class Solution:
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        mp = {}
        
        for ele in nums:
            mp[ele] = 1+mp.get(ele, 0)
            
        lst = sorted(mp.items(), key=lambda x:-x[1])
        
        result = []
        
        for i in range(K):
            result.append(lst[i][0])
            
        return result
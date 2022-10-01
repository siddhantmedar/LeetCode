class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict()
        
        for ele in nums:
            mp[ele] = 1+mp.get(ele, 0)
        
        bucket = [[] for _ in range(len(nums)+1)]
        
        for key,val in mp.items():
            bucket[val].append(key)
        
        result = []
        
        for i in range(len(bucket)-1,-1,-1):
            b = bucket[i]
            
            if b:
                for key in b:
                    if k == 0:
                        break
                        
                    result.append(key)
                    k-=1
        
        return result
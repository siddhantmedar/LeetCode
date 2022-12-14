class Solution:
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        mp = dict()
        
        for ele in nums:
            mp[ele]=1+mp.get(ele,0)
        
        box = [set() for _ in range(len(nums)+1)]
        
        for k,v in mp.items():
            box[v].add(k)
            
        result = []
        
        for i in range(len(box)-1,-1,-1):
            curr = box[i]
            
            if curr:
                for ele in curr:
                    if K == 0:
                        break
                    result.append(ele)
                    K-=1
                    
        return result
class Solution:
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        box = [[] for _ in range(10001)]
        
        mp = dict()
        
        for ele in nums:
            mp[ele] = 1 + mp.get(ele, 0)
        
        for k,v in mp.items():
            box[v].append(k)
        
        # print([(i,b) for i,b in enumerate(box) if b])
        
        result = []
        
        for i in range(len(box)-1, -1, -1):
            if box[i]:
                for ele in box[i]:
                    if K == 0:
                        break
                    print(K, ele)
                    result.append(ele)
                    K-=1
                    
            
        print(result)
        
        return result
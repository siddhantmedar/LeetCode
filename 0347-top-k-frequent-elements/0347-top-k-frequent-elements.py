class Solution:
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        mp = Counter(nums)
        
        mx = mp[max(mp,key=mp.get)]
        
        box = [[] for _ in range(mx+1)]
        print(mx+1,mp)
        
        for k,v in mp.items():
            box[v].append(k)
        
        print(box)
        
        result = []
        
        for i in range(len(box)-1,-1,-1):
#             if K==0:
#                 break
            
            cont = box[i]
            
            for ele in cont:
                if K == 0:
                    break
                result.append(ele)
                K-=1
        
        return result
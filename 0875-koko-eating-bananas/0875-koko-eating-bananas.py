class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(mid):
            time = 0
            
            for p in piles:
                time+=ceil(p/mid)
            
            print(mid, time<=h)
            return time<=h
        
        
        def bs(s,e):
            nonlocal result
            if s>e:
                return
            
            mid=(s+e)>>1
            
            if check(mid):
                result = mid
                bs(s,mid-1)
            else:
                bs(mid+1,e)
                
        
        result = None
        
        bs(1,max(piles))
        
        return result
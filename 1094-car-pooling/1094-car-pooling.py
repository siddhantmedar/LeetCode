class Solution:
    def carPooling(self, trips: List[List[int]], cap: int) -> bool:
        lst = [0 for _ in range(1001)]

        for p,_,_ in trips:
            if p>cap:
                return False
        
        for p,s,d in trips:
            for i in range(s,d):
                lst[i]+=p
                if lst[i] > cap:
                    return False
        
        return True
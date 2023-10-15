class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        st = None
        
        left,right = [], []
        
        for i,ele in enumerate(seats):
            if ele == 0:
                left.append(float("inf") if st == None else abs(st-i))
            else:
                st = i
                left.append(float("inf"))
                
        st = None
        
        for i,ele in reversed(list(enumerate(seats))):
            if ele == 0:
                right.append(float("inf") if st == None else abs(st-i))
            else:
                st = i
                right.append(float("inf"))
             
        res = float("-inf")
        
        for a,b in zip(left,right[::-1]):
            if a != float("inf") or b != float("inf"):
                res = max(res,min((a,b)))
        
        return res
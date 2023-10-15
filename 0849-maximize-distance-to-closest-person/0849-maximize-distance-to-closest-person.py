class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        st = []
        
        left,right = [], []
        
        for i,ele in enumerate(seats):
            if ele == 0:
                if not st:
                    left.append(float("inf"))
                else:
                    left.append(abs(st[-1]-i))
            else:
                st.append(i)
                left.append(float("inf"))
                
        st.clear()
        
        for i,ele in reversed(list(enumerate(seats))):
            if ele == 0:
                if not st:
                    right.append(float("inf"))
                else:
                    right.append(abs(st[-1]-i))
            else:
                st.append(i)
                right.append(float("inf"))
        
        
        res = float("-inf")
        
        for a,b in zip(left,right[::-1]):
            if a != float("inf") or b != float("inf"):
                res = max(res,min((a,b)))
        
        return res
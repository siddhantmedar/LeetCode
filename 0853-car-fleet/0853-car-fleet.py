class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lst = [(p,s) for p,s in zip(position,speed)]
        
        lst.sort()
        
        st = []
        
        for x in lst[::-1]:
            st.append((target-x[0])/x[1])
            if len(st) >= 2:
                b = st.pop()
                a = st.pop()
                
                if b <= a:
                    # intersect
                    st.append(a)
                else:
                    st.append(a)
                    st.append(b)
        
        return len(st)
                    
        
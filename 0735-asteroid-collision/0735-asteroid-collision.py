class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        
        for ele in asteroids:
            if not st:
                st.append(ele)
                
            else:
                if (st[-1] > 0 and ele < 0):
                    while st:
                        tmp = st.pop()
                        
                        if abs(tmp) == abs(ele):
                            break
                        
                        winner = tmp if abs(tmp) > abs(ele) else ele
                        
                        if not st or (st and ((st[-1] > 0 and winner > 0) or (st[-1] < 0))):
                            st.append(winner)
                            break
                            
                else:
                    st.append(ele)
                    
        return st
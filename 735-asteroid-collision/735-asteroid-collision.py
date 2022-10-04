class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        
        for ele in asteroids:
            if not st or (st and st[-1] > 0 and ele > 0) or (st and st[-1] < 0 and ele < 0):
                st.append(ele)
                
            else:
                equal = False
                
                while st and ((st[-1] > 0 and ele < 0)):
                    tmp = st.pop()
                    
                    if tmp + ele == 0:
                        equal = True
                        break
                    ele = ele if abs(ele) > abs(tmp) else tmp
                
                if not equal:
                    st.append(ele)
                        
        print(st)
        
        return st
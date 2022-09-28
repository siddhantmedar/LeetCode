class Solution:
    def merge(self, nums: List[List[int]]) -> List[List[int]]:
        nums.sort()
        
        st = [nums[0]]
        
        for i in nums[1:]:
            if st[-1][1] >= i[0]:
                last = st.pop()
                
                start, end = min(last[0],i[0]), max(last[1], i[1])
                st.append([start, end])
                
            else:
                st.append(i)
                
        return st
    
        # [[1,6],[8,10],[15,18]]
            
            
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        
        result = 0
        
        i = 0
        
        for j,ele in enumerate(s):
            if ele not in st:
                st.add(ele)
                
            elif ele in st:
                result = max(result,j-i)
                
                while ele in st:
                    st.remove(s[i])
                    i+=1
                    
                st.add(ele)
                
        result = max(result, len(st))
        
        return result
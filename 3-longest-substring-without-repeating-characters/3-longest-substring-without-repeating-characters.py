class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        result = 0
        st = set()
        
        for j in range(len(s)):
            ele = s[j]
            
            if ele not in st:
                st.add(ele)
                continue
                
            else:
                result = max(result, j-i)
                
                while ele in st:
                    st.remove(s[i])
                    i+=1
                    
                st.add(ele)
        
        result = max(result, len(s)-i)
        
        print(result)
        
        return result
      
        
#       j p w w k e w
#       i       _
#         0 1 2 3 4 5
        
#         st = { k e w}
        
#         result = 2, 3, 3
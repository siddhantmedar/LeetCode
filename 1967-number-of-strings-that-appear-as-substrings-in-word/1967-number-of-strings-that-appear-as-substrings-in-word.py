class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        st = set()
        
        for i in range(len(word)):
            s = ""
            for j in range(i, len(word)):
                s+=word[j]
                
                st.add(s)
            
        for p in patterns:
            if p in st:
                count+=1
                    
        return count
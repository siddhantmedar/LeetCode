class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        st = set([chr(i) for i in range(97, 123)])
        
        for c in sentence:
             if c in st:
                st.remove(c)
                
        return len(st) == 0
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        last = s[-1]
        
        i = 0
        
        while i < len(last) and last[i] != " ":
            i+=1
            
        return i
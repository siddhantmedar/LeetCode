class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        container = [0]*26
        
        for c in s:
            container[ord(c)-ord('a')]+=1
            
        for c in t:
            container[ord(c)-ord('a')]-=1
            
        return all([x == 0 for x in container])
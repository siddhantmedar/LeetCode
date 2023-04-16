class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        def check(c):
            if c in set(["a","e","i","o","u"]):
                return True
            
            return False
        
        
        cnt = 0
        
        for word in words[left:right+1]:
            if check(word[0]) and check(word[-1]):
                cnt+=1
                
        return cnt
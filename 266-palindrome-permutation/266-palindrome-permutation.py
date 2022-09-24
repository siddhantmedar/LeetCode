class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        mp = defaultdict()
        
        for c in s:
            mp[c] = 1+mp.get(c,0)
            
        count = 0
        
        for k,v in mp.items():
            if v%2:
                count+=1
        
        return True if count <= 1 else False
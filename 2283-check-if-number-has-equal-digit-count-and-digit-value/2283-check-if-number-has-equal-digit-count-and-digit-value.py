class Solution:
    def digitCount(self, num: str) -> bool:
        mp = {}
        
        for c in num:
            mp[int(c)] = 1+mp.get(int(c),0)
        
        for i, c in enumerate(num):
            count = mp.get(i, 0)
            if int(count) != int(c):
                return False
        
        return True
    
    # 1 2 1 0
    # 0 1 2 3
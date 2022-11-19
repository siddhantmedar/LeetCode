class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        result = float("-inf")
        mp = {}
        
        i = 0
        
        for j,c in enumerate(fruits):
            if len(mp) < 2:
                mp[c] = 1+mp.get(c,0)
                  
            elif len(mp) == 2:
                if c in mp:
                    mp[c] = 1+mp.get(c,0)
                else:
                    while len(mp) == 2:
                        result = max(result,j-i)
                        mp[fruits[i]]-=1
                        
                        if mp[fruits[i]] == 0:
                            del mp[fruits[i]]
                            
                        i+=1
                        
                    mp[c] = 1+mp.get(c,0)
        
        if len(mp) <= 2:
            result = max(result,len(fruits)-i)
            
        return result
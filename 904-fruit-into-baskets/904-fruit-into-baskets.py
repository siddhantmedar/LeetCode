class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mp = {}
        
        result = 0
        
        i = 0
        
        for j,ele in enumerate(fruits):
            if ele not in mp:
                if len(mp) < 2:
                    mp[ele] = 1+mp.get(ele, 0)
                    
                else:
                    if len(mp) == 2:
                        result = max(result, sum([v for _,v in mp.items()]))
                        
                        while len(mp) == 2:
                            mp[fruits[i]]-=1
                        
                            if mp[fruits[i]] == 0:
                                del mp[fruits[i]]
                            
                            i+=1
                        
                        mp[ele] = 1+mp.get(ele, 0)
                
            elif ele in mp:
                mp[ele] = 1+mp.get(ele, 0)
                
        if len(mp) <= 2:
            result = max(result, sum([v for _,v in mp.items()]))
            
        print(mp)
        
        return result
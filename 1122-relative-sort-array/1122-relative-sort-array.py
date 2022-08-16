class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp = {x:0 for x in arr2}
        
        res = []
        misc = []
        
        for ele in arr1:
            if ele in mp:
                mp[ele] = 1+mp.get(ele,0)
            elif ele not in mp:
                misc.append(ele)
                
        for k,v in mp.items():
            while v:
                res.append(k)
                v-=1
                
        return res+sorted(misc)
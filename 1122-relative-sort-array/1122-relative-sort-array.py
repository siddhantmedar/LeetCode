class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp = {x:0 for x in arr2}
        container = [0]*1001
        
        res = []
        misc = []
        
        for ele in arr1:
            if ele in mp:
                mp[ele] = 1+mp.get(ele,0)
            elif ele not in mp:
                container[ele]+=1
                
        for k,v in mp.items():
            while v:
                res.append(k)
                v-=1
        
        for ele, count in enumerate(container):
            while count:
                misc.append(ele)
                count-=1
    
        return res+misc
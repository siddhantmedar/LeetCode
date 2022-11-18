class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def solve():
            nonlocal result,path
            
            if len(path) == len(nums):
                result.append(copy.deepcopy(path))
            
            for key in mp:
                if mp[key]:
                    path.append(key)
                    mp[key]-=1
                    
                    solve()
                    
                    path.pop()
                    mp[key]+=1
            
            
        mp = {}
        
        for ele in nums:
            mp[ele] = 1+mp.get(ele,0)
            
        result,path = [],[]
        
        solve()
        
        return result
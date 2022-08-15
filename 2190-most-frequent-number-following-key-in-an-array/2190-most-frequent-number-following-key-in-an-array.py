class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        mp = {}
        
        for i in range(len(nums)-1):
            if nums[i] == key:
                mp[nums[i+1]] = 1+mp.get(nums[i+1],0)
                
        mx = float("-inf")
        res = None
        
        for k,v in mp.items():
            if v > mx:
                mx = v
                res = k
                
        return res
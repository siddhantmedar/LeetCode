class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        mp = {}
        
        for ele in nums:
            mp[ele] = 1+mp.get(ele,0)
        
        count = 0
        left = 0
        
        for k,v in mp.items():
            while v>=2:
                v-=2
                count+=1
                
            left+=v
            
        return [count, left]
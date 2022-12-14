class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        mp = {}
        
        for ele in nums:
            mp[ele]=1+mp.get(ele,0)
        
        mx = float("-inf")
        result = None
        
        for k,v in mp.items():
            if k%2==0 and v > mx:
                result = k
                mx = v
                
            elif k%2==0 and (v==mx and k < result):
                result = k
        
        return result if result != None else -1
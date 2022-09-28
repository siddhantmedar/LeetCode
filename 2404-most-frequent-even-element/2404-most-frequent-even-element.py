class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        mp = {}
        
        for ele in nums:
            if not ele%2:
                mp[ele] = 1+mp.get(ele, 0)
                
        mp = dict(sorted(mp.items(), key=lambda x:(-x[1], x[0])))
        
        print(mp)
        
        for k,v in mp.items():
            if not k%2:
                return k
            
        return -1
        
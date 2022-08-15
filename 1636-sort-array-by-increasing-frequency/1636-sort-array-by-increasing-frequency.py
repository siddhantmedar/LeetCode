class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mp = {}
        
        for ele in nums:
            mp[ele] = 1+mp.get(ele,0)
            
        nums.sort(key=lambda x:(mp[x],-x))
        
        return nums
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
        
#         for i in range(len(nums)-1):
#             if nums[i] == nums[i+1]:
#                 return True
            
#         return False
        
        mp = {}
        
        for ele in nums:
            mp[ele] = 1+mp.get(ele, 0)
            
        for k,v in mp.items():
            if v>=2:
                return True
            
        return False
        
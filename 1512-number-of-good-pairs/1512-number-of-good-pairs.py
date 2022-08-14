class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j]:
#                     count+=1
                    
#         return count
            
        mp = {x:0 for x in nums}
        
        for ele in nums:
            mp[ele] = 1+mp.get(ele,0)
            
        count = 0
        
        for _, v in mp.items():
            if v>1:
                count+=((v*(v-1))//2)
                
        return count
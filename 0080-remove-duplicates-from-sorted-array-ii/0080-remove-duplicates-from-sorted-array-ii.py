class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mp = dict()
        
        for ele in set(nums):
            mp[ele]=2
            
        i,j = 0,0
        
        while j<len(nums):
            if mp[nums[j]] > 0:
                nums[i] = nums[j]
                i+=1
                mp[nums[j]]-=1
            
            j+=1
            
        # print(i)
        
        return i
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = len(nums)-1
        
        while idx>0 and nums[idx-1]>=nums[idx]:
            idx-=1
            
        idx-=1
        
        if idx>=0:
            j = len(nums)-1

            while j>=0 and nums[idx] >= nums[j]:
                j-=1
            
            nums[idx],nums[j] = nums[j],nums[idx]
        
        low,high = idx+1,len(nums)-1
        
        while low<high:
            nums[low],nums[high] = nums[high],nums[low]
            low+=1
            high-=1
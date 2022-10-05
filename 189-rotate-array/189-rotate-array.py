class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result = [0 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            result[(i+k)%len(nums)] = nums[i]
            
        # print(result)
        
        for i in range(len(nums)):
            nums[i] = result[i]
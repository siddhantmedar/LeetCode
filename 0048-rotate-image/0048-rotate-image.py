class Solution:
    def rotate(self, nums: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        l,r = 0, len(nums[0])-1
        
        for _ in range(len(nums)//2):
            t,b = l,r
            
            for i in range(r-l):
                tmp = nums[t][l+i]
                nums[t][l+i] = nums[b-i][l]
                nums[b-i][l] = nums[b][r-i]
                nums[b][r-i] = nums[t+i][r]
                nums[t+i][r] = tmp
                
            l+=1
            r-=1
        
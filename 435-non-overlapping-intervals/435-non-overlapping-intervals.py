class Solution:
    def eraseOverlapIntervals(self, nums: List[List[int]]) -> int:
        nums.sort()
        
        print(nums)
        
        end = nums[0][1]
        count = 0
        
        for i in nums[1:]:
            if i[0] < end:
                count+=1
                end = min(end, i[1])
            else:
                end = i[1]
                
        print(count)
        
        return count
    
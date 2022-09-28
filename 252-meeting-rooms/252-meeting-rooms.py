class Solution:
    def canAttendMeetings(self, nums: List[List[int]]) -> bool:
        nums.sort(key=lambda x:x[0])
        
        for i in range(len(nums)-1):
            if nums[i][1] > nums[i+1][0]:
                return False
        
        return True
class Solution:
    def canAttendMeetings(self, nums: List[List[int]]) -> bool:
        nums.sort(key=lambda x:x[0])
        
        for i in range(len(nums)-1):
            e1, e2 = nums[i], nums[i+1]
            
            if e1[1] > e2[0]:
                return False
            
        return True
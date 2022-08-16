class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        @cmp_to_key
        def cmp(x,y):
            x = str(x)+str(y)
            y = str(y)+str(x)
            
            if x > y:
                return -1
            
            elif x < y:
                return 1
            
            else:
                return 0
            
            
        nums.sort(key=cmp)
        
        return "".join([str(x) for x in nums]) if nums[0] != 0 else "0"
        
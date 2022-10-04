class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        @cmp_to_key
        def cmp(x,y):
            x = str(x)
            y = str(y)
            
            x+=y
            y+=x
            
            if x > y:
                return -1
            
            elif x == y:
                return 0
            
            elif x < y:
                return 1
        
        nums.sort(key=cmp)

        return "".join([str(x) for x in nums]) if nums[0] != 0 else "0"
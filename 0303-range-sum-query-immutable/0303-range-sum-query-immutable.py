class NumArray:

    def __init__(self, nums: List[int]):
        self.res= [0 for _ in range(len(nums))]
        self.res[0] = nums[0]
        
        for i in range(1,len(nums)):
            self.res[i] = nums[i]+self.res[i-1]

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.res[right]
        
        return self.res[right] - self.res[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
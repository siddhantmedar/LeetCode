class NumArray:

    def __init__(self, nums: List[int]):
        self.left = [0 for _ in range(len(nums))]
        
        self.left[0] = nums[0]
        
        for i in range(1, len(self.left)):
            self.left[i] = self.left[i-1] + nums[i]
        
    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.left[right] - self.left[left-1]
        elif left == 0:
            return self.left[right]
        
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, ele in enumerate(nums):
            if ele == target:
                return i
            
        return -1
        
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return list(set([x for x in range(0, len(nums)+1)]).difference(set(nums)))[0]
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        def kadanes(nums):
            curr_sum = nums[0]
            best_sum = nums[0]

            for i in range(1, len(nums)):
                curr_sum = max(curr_sum+nums[i], nums[i])
                best_sum = max(curr_sum ,best_sum)

            return best_sum


        if k == 1:
            result = kadanes(arr)
            return result % (10**9 + 7)

        else:
            sm = sum(arr)

            if sm < 0:
                result = kadanes(arr+arr)
                return result % (10**9 + 7) if result >= 0 else 0
            else:
                result = kadanes(arr+arr)+(k-2)*sm
                return result % (10**9 + 7)
class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        res = 0
        st = []

        for i in range(len(nums)+1):
            while st and (i == len(nums) or nums[st[-1]] >= nums[i]):
                height = nums[st.pop()]

                if not st:
                    width = i

                else:
                    width = i-st[-1]-1

                res = max(res, width*height)

            st.append(i)

        return res
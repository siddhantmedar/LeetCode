class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def solve(nums):
            st = []

            leftSmaller = deque()
            rightSmaller = deque()

            for i in range(len(nums)):
                ele = nums[i]

                while st and nums[st[-1]] >= ele:
                    st.pop()
                if not st:
                    leftSmaller.append(0)
                else:
                    leftSmaller.append(st[-1] + 1)
                st.append(i)

            st.clear()

            for i in range(len(nums) - 1, -1, -1):
                ele = nums[i]

                while st and nums[st[-1]] >= ele:
                    st.pop()

                if not st:
                    rightSmaller.appendleft(len(nums) - 1)
                else:
                    rightSmaller.appendleft(st[-1] - 1)
                st.append(i)

            res = 0

            for i in range(len(nums)):
                res = max(res, (rightSmaller[i] - leftSmaller[i] + 1) * nums[i])

            return res

        result = 0
        
        frame = [0 for _ in range(len(matrix[0]))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    frame[j]+=1
                    
                else:
                    frame[j] = 0
            
            result = max(result, solve(frame))
            
        return result
    
    # [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    # 1 0 1 0 0
    # 2 0 2 1 1
    # 3 1 3 2 2
    # 4 0 0 3 0
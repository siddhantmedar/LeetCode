class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def solve(nums):
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
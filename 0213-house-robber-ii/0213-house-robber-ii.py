class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(idx,nms):
            if idx>=len(nms):
                    return 0
            
            if dp[idx] != -1:
                return dp[idx]
            
            dp[idx] = max(solve(idx+2, nms) +nms[idx], solve(idx+1,nms))
            
            return dp[idx]
        
        if len(nums) <= 2:
            return max(nums)
        
        dp = [-1 for _ in range(len(nums))]
        op1 = solve(0,nums[:-1])
        
        dp = [-1 for _ in range(len(nums))]
        op2 = solve(0,nums[1:])

        return max(op1, op2)
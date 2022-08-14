class Solution:
    def trap(self, heights: List[int]) -> int:
        left, right = [0]*len(heights), [0]*len(heights)
        
        for i in range(1, len(heights)):
                left[i] = max(left[i-1], heights[i-1])
                
        for i in range(len(heights)-2,-1,-1):
                right[i] = max(right[i+1], heights[i+1])
                
        result = 0
        
        for i in range(1,len(heights)-1):
            if min(left[i], right[i]) < heights[i]:
                continue
                
            result+=(min(left[i], right[i])-heights[i])
        
        return result
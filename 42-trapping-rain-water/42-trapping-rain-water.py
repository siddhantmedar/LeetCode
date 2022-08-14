class Solution:
    def trap(self, heights: List[int]) -> int:
        start, end = 0, len(heights)-1
        left, right = heights[0], heights[len(heights)-1]
        
        result = 0
        
        while start < end:
            if left <= right:
                start+=1
                
                if left-heights[start] >=0:
                    result+=(left-heights[start])
                left = max(left, heights[start])
            
            else:
                end-=1
                if right-heights[end] >= 0:
                    result+=(right-heights[end])
                right = max(right, heights[end])
            
        return result
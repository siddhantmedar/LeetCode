class Solution:
    def trap(self, height: List[int]) -> int:
        height = [0]+height+[0]
        
        result = 0
        
        for i in range(1, len(height)-1):
            left = max(height[:i])
            right = max(height[i:])
            
            water = min(right,left)-height[i]
            
            if water>0:
                result+= water
            
        return result
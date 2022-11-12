class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        
        low, high = 0, len(height)-1

        while low < high:
            result = max(result, (high-low)*min(height[low],height[high]))
            
            if height[low] <= height[high]:
                low+=1
                
            else:
                high-=1
                
        return result
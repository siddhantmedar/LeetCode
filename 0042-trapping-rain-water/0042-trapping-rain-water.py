class Solution:
    def trap(self, height: List[int]) -> int:
        height = [0]+height+[0]
        left = [0 for _ in range(len(height))]
        right = [0 for _ in range(len(height))]
        
        for i in range(1,len(height)-1):
            left[i] = max(left[i-1],height[i-1])
        
        for i in range(len(height)-2,-1,-1):
            right[i] = max(right[i+1],height[i+1])    

        result = 0
        
        for i in range(len(height)):
            water = min(left[i],right[i])-height[i]
            print(water)
            if water>0:
                result+=water
                
        return result
        
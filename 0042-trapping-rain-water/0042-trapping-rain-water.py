class Solution:
    def trap(self, height: List[int]) -> int:
        left =[0]*len(height)
        right = [0]*len(height)
        
        left[0] = height[0]
        right[len(height)-1] = height[len(right)-1]
        
        for i in range(1,len(left)):
            left[i] = max(left[i-1],height[i])
            
        for i in range(len(right)-2,-1,-1):
            right[i] = max(right[i+1],height[i])
            
        result = 0
        
        for i in range(len(height)):
            water = min(left[i],right[i])-height[i]
            result+=water if water>=0 else 0
            
        return result
class Solution:
    def trap(self, height: List[int]) -> int:
        low,high=0,len(height)-1
        
        result = 0
        
        mxl,mxr = height[low],height[high]
        
        while low<high:
            if height[low]<=height[high]:
                low+=1
                
                water = min(mxl,mxr)-height[low]
                
                if water>=0:
                    result+=water
                
                mxl = max(mxl,height[low])
            else:
                high-=1
                
                water = min(mxl,mxr)-height[high]
                
                if water>=0:
                    result+=water
                
                mxr = max(mxr,height[high])
                
        return result
                
                
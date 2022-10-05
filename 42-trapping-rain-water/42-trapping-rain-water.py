class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        
        mxl, mxr = height[l], height[r]
        
        result = 0
        
        while l<r:
            if height[l] <= height[r]:
                l+=1
                
                if min(mxl, mxr)-height[l] > 0:
                    result+=min(mxl, mxr)-height[l]
                
                mxl = max(mxl, height[l])
            else:
                r-=1
                
                if min(mxl, mxr)-height[r] > 0:
                    result+=min(mxl, mxr)-height[r]
                    
                mxr = max(mxr, height[r])
                
        return result
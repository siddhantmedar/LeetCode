class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
#         for i in range(len(arr)-1):
#             if arr[i] > arr[i+1]:
#                 return i
        
        low,high = 0,len(arr)-1
        
        
        while low < high:
            mid=(low+high)>>1
            
            if arr[mid] < arr[mid+1]:
                low = mid+1
            else:
                high = mid
                
        return low
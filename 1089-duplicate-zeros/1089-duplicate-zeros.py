class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if arr[i] != 0:
                i+=1
                continue
                
            elif arr[i] == 0:
                idx=i+1
                put = 0
                tmp = None
                
                while idx < len(arr):
                    tmp = arr[idx]
                    arr[idx] = put
                    
                    put = tmp
                    
                    idx+=1
                
                i+=1
            
            i+=1
                    
        
                    
                
        
        
#         [1,0|,0,2,3,0,4,5]
#                         _   
#             put = 0
#             tmp = 0
            
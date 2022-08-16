class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        
        for ele1 in arr1:
            first_time = True
            for ele2 in arr2:
                if abs(ele1-ele2) <= d:
                    if first_time:
                        count+=1
                        first_time = False
                    
        return len(arr1)-count
        
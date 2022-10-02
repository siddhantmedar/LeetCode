class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        @cmp_to_key
        def cmp(a,b):
            if abs(a-x) < abs(b-x):
                return -1
            
            elif abs(a-x) == abs(b-x):
                return 0
            
            elif abs(a-x) > abs(b-x):
                return 1
            
            
        arr.sort(key=cmp)
        
        print(arr)
        
        return sorted(arr[:k])
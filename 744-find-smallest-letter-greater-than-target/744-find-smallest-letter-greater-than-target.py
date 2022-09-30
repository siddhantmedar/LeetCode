class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # mp = {i:chr(ord('a')+i) for i in range(1,27)}
        
        result = None
        
        start, end = 0, len(letters)-1
        
        while start <= end:
            mid = (start+end)>>1
            
            if letters[mid] > target:
                result = letters[mid]
                end = mid-1
            
            else:
                start = mid+1
                
        return result if result else letters[0]
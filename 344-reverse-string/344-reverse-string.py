class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tmp = list(s)
        
        start, end = 0, len(s)-1
        
        while start <= end:
            tmp[start], tmp[end] = tmp[end], tmp[start]
            start+=1
            end-=1
            
        s[::] = "".join(tmp)
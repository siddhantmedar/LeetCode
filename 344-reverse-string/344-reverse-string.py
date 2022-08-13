class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rev(start, end):
            if start > end:
                return
            
            s[start], s[end] = s[end], s[start]
            
            rev(start+1, end-1)
            
        rev(0, len(s)-1)
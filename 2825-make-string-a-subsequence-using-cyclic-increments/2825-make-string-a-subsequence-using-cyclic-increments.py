class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i,j= 0, 0
        
        while i<len(str1) and j<len(str2):
            nxt = ord(str1[i])
            
            if nxt+1 <= 122:
                nxt+=1
                nxt = chr(nxt)
            else:
                nxt = 'a'
            
            if str1[i] == str2[j] or nxt == str2[j]:
                j+=1
            i+=1

        return j == len(str2)
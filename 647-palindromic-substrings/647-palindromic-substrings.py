class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalin(word):
            s,e = 0, len(word)-1
            
            while s<=e:
                if word[s] != word[e]:
                    return False
                s+=1
                e-=1
                
            return True
        def check(l,r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                lst.append(s[l:r+1])
                
                l-=1
                r+=1
        
        lst = list()
        
        for i in range(len(s)):
            check(i,i)

            if i+1 < len(s):
                check(i, i+1)
            
        # print(lst)
        
        return len(lst)
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def solve(idx):
            if idx == len(s):
                result.append("".join(lst))
                return
                
            if s[idx].isalpha():
                lst.append(s[idx].lower())
                solve(idx+1)
                lst.pop()
                
                lst.append(s[idx].upper())
                solve(idx+1)
                lst.pop()
                
            else:
                lst.append(s[idx])
                solve(idx+1)
                lst.pop()
                
        
        lst = deque()
        result = []
        
        solve(0)
        
        return result
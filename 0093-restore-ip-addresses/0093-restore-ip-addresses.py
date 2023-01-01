class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def solve(idx,path,dots):
            nonlocal res
            
            if idx >= len(s):
                if dots == 0:
                    res.add(path[:][:-1])
                return
            
            # print(idx)
            
            for i in range(idx,idx+3):
                if 0<=int(s[idx:i+1])<=255 and \
                (len(s[idx:i+1])==1 or (len(s[idx:i+1]) > 1 and int(s[idx]) != 0)):
                    solve(i+1,path+s[idx:i+1]+".",dots-1)
        
        
        res = set()
        
        solve(0,"",4)
        
        return list(res)
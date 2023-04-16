class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        mx, res = float("-inf"), None
        
        for i in range(len(mat)):
            cnt = 0
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    cnt+=1
            
            if cnt == mx:
                res = min(res,i)
                
            if cnt > mx:
                mx = cnt
                res = i
                
        return [res,mx]
                    
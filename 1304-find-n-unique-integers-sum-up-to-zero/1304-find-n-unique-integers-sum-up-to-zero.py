class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = deque()
        
        if n%2:
            result.appendleft(0)
            
        num = 1
        
        while len(result) != n:
            result.append(num)
            
            if len(result)==n:
                break
            
            result.append(-num)
            
            if len(result)==n:
                break
                
            num+=1
                
        return result
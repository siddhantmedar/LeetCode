class Solution:
    def average(self, salary: List[int]) -> float:
        mx, mn = max(salary), min(salary)
        
        sm, count = 0, 0
        
        for s in salary:
            if s != mx and s != mn:
                sm+=s
                count+=1
                
        return sm/count
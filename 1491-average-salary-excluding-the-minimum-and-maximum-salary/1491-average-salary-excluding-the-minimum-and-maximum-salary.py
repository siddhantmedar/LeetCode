class Solution:
    def average(self, salary: List[int]) -> float:
        mn = float("inf")
        mx = float("-inf")
        
        for sal in salary:
            if mn > sal:
                mn = sal
            if mx < sal:
                mx = sal
                
        return (sum(salary)-mn-mx)/(len(salary)-2)
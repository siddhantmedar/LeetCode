class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:(x[0]-x[1]))
        
        res = 0
        
        for i in range(len(costs)//2):
            res+=costs[i][0]
            
        for i in range(len(costs)//2, len(costs)):
            res+=costs[i][1]
            
        return res
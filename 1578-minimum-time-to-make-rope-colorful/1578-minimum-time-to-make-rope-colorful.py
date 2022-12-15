class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i,j = 0,0
        result = 0
        
        while i<len(neededTime) and j<len(neededTime):
            total = 0
            mx = 0
            
            
            while j<len(neededTime) and colors[i]==colors[j]:
                total+=neededTime[j]
                mx = max(mx,neededTime[j])
                j+=1
                
            result+=total-mx
            
            i=j
            
        return result
            
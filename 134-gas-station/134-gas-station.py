class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr_gas = 0
        total_gas = 0
        
        starting_point = 0
        
        for i in range(len(gas)):
            total_gas+=gas[i]-cost[i]
            curr_gas+=gas[i]-cost[i]
            
            if curr_gas < 0:
                curr_gas = 0
                starting_point = i+1
                
        return starting_point if total_gas >= 0 else -1
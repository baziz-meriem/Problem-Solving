class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        total_cost = 0
        current_gas = 0
        start_index = 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            current_gas += gas[i] - cost[i]
            
            # If current gas becomes negative, reset the starting index and current gas
            if current_gas < 0:
                start_index = i + 1
                current_gas = 0
        
        # After the loop, check if we have enough gas to cover the total cost
        if total_gas >= total_cost:
            return start_index
        else:
            return -1

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        current_gas = 0
        start_index = 0
        total_gas = 0
        
        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            total_gas += gas[i] - cost[i]
            
            # If current gas becomes negative, reset the starting index and current gas
            if current_gas < 0:
                start_index = i + 1
                current_gas = 0
        
        # If the total gas collected minus the total cost is non-negative, return start_index
        return start_index if total_gas >= 0 else -1

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        gasCost = [(gas[i], cost[i], i) for i in range(len(gas))]
        gasCost.sort(key=lambda tup: tup[0], reverse=True)
        
        # Try the best starting index from the sorted list
        for _, _, start in gasCost:
            current_gas = 0
            n = len(gas)
            for i in range(start, start + n):
                idx = i % n
                current_gas += gas[idx] - cost[idx]
                if current_gas < 0:
                    break
            else:
                return start
        
        return -1

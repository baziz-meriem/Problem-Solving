class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(start, comb):
            # If the combination is done
            if len(comb) == k:
                result.append(comb[:])
                return
            
            # Move through the numbers starting from 'start'
            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()  # Backtrack

        result = []
        backtrack(1, [])
        return result
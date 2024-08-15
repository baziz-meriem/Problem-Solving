from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_value = -1  # Initialize max_value to -1, as there are no elements to the right of the last one

        for i in range(len(arr) - 1, -1, -1):
            current_value = arr[i]
            arr[i] = max_value
            max_value = max(max_value, current_value)

        return arr

            
        
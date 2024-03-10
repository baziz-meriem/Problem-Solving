from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()  # Sorting in ascending order
        left, right = 0, len(people) - 1
        boats = 0
        
        while left <= right:
            if left == right:  # If only one person left
                boats += 1
                break
            
            if people[left] + people[right] <= limit:
                left += 1  # Both people fit in the boat
            right -= 1  # Right pointer always moves
            
            boats += 1  # Increment boat count for each pair
            
        return boats

from bisect import bisect_left
from typing import List
class Solution:

    def findRadius(self,houses: List[int], heaters: List[int]) -> int:
        # Sort the houses and heaters
        houses.sort()
        heaters.sort()
        
        def find_closest_heater_distance(house: int) -> int:
            # Find the position to insert the house in heaters
            pos = bisect_left(heaters, house)
            # Find distances to the closest heaters
            left_distance = float('inf') if pos == 0 else abs(house - heaters[pos - 1])
            right_distance = float('inf') if pos == len(heaters) else abs(house - heaters[pos])
            # Return the minimum distance to the closest heater
            return min(left_distance, right_distance)
        
        # Find the maximum distance required for all houses
        max_radius = max(find_closest_heater_distance(house) for house in houses)
        
        return max_radius

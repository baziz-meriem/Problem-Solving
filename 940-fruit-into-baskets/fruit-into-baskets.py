from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        basket_dict = {}
        left = 0

        for right, fruit in enumerate(fruits):
            basket_dict[fruit] = right

            if len(basket_dict) > 2:
                min_index = min(basket_dict.values())
                del basket_dict[fruits[min_index]]
                left = min_index + 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits

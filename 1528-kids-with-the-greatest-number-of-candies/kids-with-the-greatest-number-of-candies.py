class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        for idx,candy in enumerate(candies):
            if candy + extraCandies >= max_candies:
                candies[idx] = True
            else:
                candies[idx] = False

        return candies

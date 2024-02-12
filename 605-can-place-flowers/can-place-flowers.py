class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty_spaces = 0
        taken = True

        for plot in flowerbed:
            if plot == 0 and bool(plot) != taken:
                empty_spaces += 1
                taken = not taken

            elif plot==1 and not taken:
                empty_spaces -= 1
            else:
                 taken = not taken
            


        return empty_spaces >= n
        
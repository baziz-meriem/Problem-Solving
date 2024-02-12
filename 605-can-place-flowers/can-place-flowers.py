class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        taken = True

        for plot in flowerbed:
            if plot == 0 and bool(plot) != taken:
                n -= 1
                taken = not taken

            elif plot==1 and not taken:
                n += 1
            else:
                 taken = not taken
            


        return n<=0
        
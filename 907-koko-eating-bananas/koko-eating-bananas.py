import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        current = max(piles)
        low, high = 1, max(piles)+1

        while low<=high:
            mid = (high+low)//2
            #print(mid)
            hNeeded = 0
            for num in piles:
                hNeeded += math.ceil(num/ mid)
                if hNeeded > h:
                    break
            #print("Needed",hNeeded)
            
            if hNeeded > h:
                low = mid + 1
            else:
                high = mid - 1
                current = min(current,mid)
            #print('current is:',current)
        return current
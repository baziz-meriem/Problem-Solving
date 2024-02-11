class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_pivot=[]
        greater_pivot=[]
        piv_duplicates = 0
        for num in nums:
            if num < pivot:
                less_pivot.append(num)
            elif num> pivot:
                greater_pivot.append(num)
            else:
                piv_duplicates += 1
        #add the pivot and it's duplicates in the list
        less_pivot.extend([pivot]*piv_duplicates)
        
        return less_pivot + greater_pivot
            
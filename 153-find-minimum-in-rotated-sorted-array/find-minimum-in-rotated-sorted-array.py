import heapq
class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = float('inf')
        high = len(nums)-1
        low = 0
        while low<=high:
            mid = (high+low)//2
           
            if nums[mid] >= nums[low]:
                min_val = min(min_val,nums[low])
                low = mid+1

            else:
                min_val = min(min_val,nums[mid])
                high = mid -1
        return min_val
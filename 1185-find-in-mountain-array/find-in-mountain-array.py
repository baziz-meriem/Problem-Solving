# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        def find_peak(n):
            left = 0
            right = n - 1

            while left <= right:
                mid = left + (right - left) // 2

                if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid - 1
            return left


        def binary_search_ascending(left, right):
            while left <= right:
                mid = left + (right - left) // 2
                val = mountain_arr.get(mid)
                if val == target:
                    return mid
                elif target > val:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        def binary_search_descending(left, right):
            while left <= right:
                mid = left + (right - left) // 2
                val = mountain_arr.get(mid)

                if val == target:
                    return mid
                elif target > val:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        peak_index = find_peak(n)
        res = -1
        if target >= mountain_arr.get(0) and target <= mountain_arr.get(peak_index):
            res = binary_search_ascending(0, peak_index)
        
        if res == -1:
            res = binary_search_descending(peak_index + 1, n - 1)

        return res
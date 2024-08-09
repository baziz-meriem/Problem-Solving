class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #flatten matrix
        nums = [num for row in matrix for num in row]
        
        high = len(nums) -1
        low = 0
        while low <= high:
            mid = (high+low)//2
            if nums[mid] == target:
                return True
            elif nums[mid]< target:
                low = mid + 1
            else:
                high = mid - 1

        return False
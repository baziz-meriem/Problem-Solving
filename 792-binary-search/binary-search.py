class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high=len(nums)-1
        low=0
        while low<=high:
            mid = (high+low)//2
            element=nums[mid]
            
            if element == target:
                return mid
            elif element>target:
                high = mid - 1
            elif element<target:
                low = mid + 1
        return -1
            
        
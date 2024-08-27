class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = [str(e) for e in nums]

        array = sorted(arr, key=lambda x: x*10 ,reverse=True)
        result = "".join(array)
        if result[0] == "0":
            return "0"
        return result
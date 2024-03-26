class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out=[]
        current_sum=0
        for num in nums:
            current_sum += num
            out.append(current_sum)
        return out
        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        end_idx=len(numbers)-1
        start_idx=0
        
        while end_idx>-1 and start_idx<len(numbers):
            if numbers[end_idx]+numbers[start_idx]==target:
                return [start_idx+1,end_idx+1]
            elif numbers[end_idx]+numbers[start_idx]<target :
                start_idx += 1
            else:
                end_idx -= 1


        
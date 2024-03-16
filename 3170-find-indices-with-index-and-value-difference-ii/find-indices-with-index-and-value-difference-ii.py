class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:

        min_max_dict ={}
        min_max_dict[len(nums)-1] = [   [nums[len(nums)-1],len(nums)-1],#min,idx
                                        [nums[len(nums)-1],len(nums)-1]#max,idx
                                        ]
        for n in range(len(nums)-2,-1,-1):
            max_val = max(nums[n], min_max_dict[n+1][1][0])
            max_idx = n if nums[n]>min_max_dict[n+1][1][0] else min_max_dict[n+1][1][1]

            min_val =  min(nums[n], min_max_dict[n+1][0][0])
            min_idx = n if nums[n]<min_max_dict[n+1][0][0] else min_max_dict[n+1][0][1]

            min_max_dict[n] = [[min_val,min_idx],[max_val,max_idx]]
       

        for idx,val in enumerate(nums[:len(nums)-indexDifference]):
            max_val = min_max_dict[idx+indexDifference][1][0]
            idx_max = min_max_dict[idx+indexDifference][1][1]

            min_val = min_max_dict[idx+indexDifference][0][0]
            idx_min = min_max_dict[idx+indexDifference][0][1]

            if abs(max_val-val)>= valueDifference:
                return [idx,idx_max]

            elif abs(min_val-val)>= valueDifference:
                return [idx,idx_min]
            else:
                continue
        return [-1,-1]
        
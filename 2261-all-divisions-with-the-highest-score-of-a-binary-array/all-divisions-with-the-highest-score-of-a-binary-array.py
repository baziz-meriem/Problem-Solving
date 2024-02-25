class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        zeros_count = 0
        ones_count = nums.count(1)
        dict_max_score = {ones_count:{0}}

        for idx,value in enumerate(nums):
            if value ==0:
                zeros_count += 1
            else:
                ones_count -= 1 

            current_sum = zeros_count + ones_count
            
            if current_sum > max(dict_max_score.keys()):
                del dict_max_score[max(dict_max_score.keys())]
                dict_max_score[current_sum] = {idx+1}

            elif current_sum == max(dict_max_score.keys()):
                dict_max_score[current_sum].add(idx+1)
            

        return list(dict_max_score.values())[0]
        
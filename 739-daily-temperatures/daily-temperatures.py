from collections import defaultdict
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_dict = defaultdict(int)
        temp_stack=[]

        for idx, temp in enumerate(temperatures):
            while temp_stack and temp> temp_stack[-1][0]:
                prev_temp,stack_idx = temp_stack.pop()
                temp_dict[stack_idx] = idx-stack_idx 
            temp_stack.append([temp,idx])
        print(temp_dict)
        return [temp_dict[idx] for idx in range(len(temperatures))]
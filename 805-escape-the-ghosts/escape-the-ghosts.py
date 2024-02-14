import numpy as np
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        x_target = target[0]
        y_target = target[1]
        #caculate steps for me to reach goal
        my_steps = abs(x_target)+abs(y_target)
        #calculate steps for goast to reach me
        for x_ghost,y_ghost in ghosts:
           
            if abs(x_ghost -x_target)+abs(y_ghost -y_target) <= my_steps:
                return False
                
        return True
        
        
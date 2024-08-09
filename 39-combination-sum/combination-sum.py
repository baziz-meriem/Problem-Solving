class Solution:
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations=[]
        def backtracking(idx,curr):
            if sum(curr) == target:
                combinations.append(curr[:])
                #print('combinations',combinations)
                return
            elif sum(curr) > target:
                return
            for i in range(idx,len(candidates)):
                curr.append(candidates[i])
                #print(curr)
                backtracking(i,curr)
                curr.pop()
            
        backtracking(0,[])
        return combinations

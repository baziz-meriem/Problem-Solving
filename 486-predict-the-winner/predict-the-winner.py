from functools import cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        @cache
        def dp(i, j, turn):

            if j < i: return -math.inf

            if j - i + 1 == 1:
                return nums[i]
            
            if turn == 'p1':

                # take leftmost
                choice1 = nums[i] + dp(i+1, j, 'p2') 
                # take rightmost
                choice2 = nums[j] + dp(i, j-1, 'p2')

                return max(choice1, choice2)
            
            elif turn == 'p2':

                # take leftmost
                choice1 = dp(i+1, j, 'p1') 
                # take rightmost
                choice2 = dp(i, j-1, 'p1')

                return min(choice1, choice2)

            else:
                raise Exception('turn should be p1 or p2')


        p1_best = dp(0, len(nums)-1, 'p1')
        print(p1_best)

        return p1_best >= sum(nums) / 2
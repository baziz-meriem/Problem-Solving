class Solution:
    def guessNumber(self, n: int) -> int:
        min_val = 1
        max_val = n

        while min_val <= max_val:
            number_picked = (min_val + max_val) // 2
            out = guess(number_picked)

            if out == -1:
                max_val = number_picked - 1
            elif out == 1:
                min_val = number_picked + 1
            else:
                return number_picked

        return -1  # Not found

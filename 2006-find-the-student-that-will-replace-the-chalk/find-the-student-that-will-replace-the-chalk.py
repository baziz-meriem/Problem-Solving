class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum_chalk = sum(chalk)
        rem= k % sum_chalk
        for idx,s in enumerate(chalk):
            rem -= s
            if rem<0:
                return idx
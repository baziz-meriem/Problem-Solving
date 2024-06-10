class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def has_leading_zeros(s):
            return len(s) > 1 and s[0] == '0'

        for i in range(1, n):
            for j in range(i + 1, n):
                num1, num2 = num[:i], num[i:j]

                if has_leading_zeros(num1) or has_leading_zeros(num2):
                    continue

                while j < n:
                    sum_str = str(int(num1) + int(num2))
                    if not num.startswith(sum_str, j):
                        break
                    j += len(sum_str)
                    num1, num2 = num2, sum_str

                if j == n:
                    return True

        return False

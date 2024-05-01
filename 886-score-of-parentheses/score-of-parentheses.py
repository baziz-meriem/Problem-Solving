from collections import deque
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = deque([0])
        for car in s:
            if car == '(':
                stack.append(0)
            else:
                val = max(2*stack.pop(),1)
                stack[-1] += val 
        return stack.pop()
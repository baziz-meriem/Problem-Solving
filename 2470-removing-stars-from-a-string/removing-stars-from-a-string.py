from collections import deque
class Solution:
    def removeStars(self, s: str) -> str:
        char_stack = deque()
        for car in s:
            if car == "*" and char_stack:
                char_stack.pop()
            else:
                char_stack.append(car)
        return ''.join(list(char_stack))
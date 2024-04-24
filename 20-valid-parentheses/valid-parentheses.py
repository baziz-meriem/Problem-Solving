from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        parenthesis={']':'[',')':'(','}':'{'}
        for car in s:
            if car in parenthesis.values():
                stack.append(car)
            elif car in parenthesis:
                if not stack or stack and  stack.pop()!= parenthesis[car]:
                    return False

        
        return True if not stack else False

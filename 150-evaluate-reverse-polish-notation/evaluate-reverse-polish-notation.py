from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokens_stack = deque()
        operators='+-*/'

        for token in  tokens:
            if token in operators:
                first_num = tokens_stack.pop()
                second_num = tokens_stack.pop()

                if token=='+':
                    tokens_stack.append(first_num+ second_num)
                elif token=='-':     
                    tokens_stack.append(second_num - first_num)
                elif token=='*':
                    tokens_stack.append(first_num * second_num)
                else:
                    tokens_stack.append(int( second_num / first_num))
                
            else:
                tokens_stack.append(int(token))

        return tokens_stack.pop()
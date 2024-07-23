from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:

        strStack = deque()
        tempStr=[]
        for car in s:
            print(strStack)
            if car != "]":
                strStack.append(car)
                
            else:
            
                while strStack[-1] != "[":
                    tempStr.append(strStack.pop())
                tempStr = tempStr[::-1]
                print('tempStr',tempStr)

                #pop [
                strStack.pop()
                k=[]
                nums=["0","1","2","3","4","5","6","7","8","9"]
                while strStack and strStack[-1] in nums:
                    k.append(strStack.pop())
                k= k[::-1]

                k = int("".join(k))
                strStack.append(k * "".join(tempStr))
                tempStr =[]
        return ''.join(strStack)

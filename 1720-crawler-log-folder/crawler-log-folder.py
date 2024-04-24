from collections import deque
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        file_sys = deque()
        for act in logs:
            if act == "../" and file_sys:
                file_sys.pop()
            elif act != "./" and act != "../": #means it's an actiion to move to a child folder
                file_sys.append(act)
        print(file_sys)
        return len(file_sys)
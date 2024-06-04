class Solution:
    def splitString(self, s):

        def dfs(start, last):
            res = False
            for k in range(1, len(s)-last+1):
                if (int(s[start:last])-int(s[last:last+k])) == 1:
                    if dfs(last, last+k):
                        return True
                    res = True
                else:
                    res = False
            return res

        for i in range(1, len(s)):
            if dfs(0, i):
                return True
                
        return False
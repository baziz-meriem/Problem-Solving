class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def remove(string):
            while '#' in string:
                a = string.index('#')
                if a == 0:
                    string = string[1:]
                else:
                    string = string[:a-1] + string[a+1:]
            return string
        
        s, t = remove(s), remove(t)
        return s == t
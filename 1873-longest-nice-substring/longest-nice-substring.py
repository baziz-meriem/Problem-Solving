class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        if len(s) < 2:
            return ""
        
        # Check if the current string is nice
        def is_nice(st):
            chars = set(st)
            for c in chars:
                if c.lower() not in chars or c.upper() not in chars:
                    return False
            return True
        
        if is_nice(s):
            return s
        
        # Recursive divide and conquer
        for i in range(len(s)):
            if s[i].lower() not in s or s[i].upper() not in s:
                left_nice = self.longestNiceSubstring(s[:i])
                right_nice = self.longestNiceSubstring(s[i+1:])
                if len(left_nice) >= len(right_nice):
                    return left_nice
                else:
                    return right_nice
        
        return ""

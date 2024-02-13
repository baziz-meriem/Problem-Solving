class Solution:
    def reverseWords(self, s: str) -> str:
        string_list = s.split()
        return ' '.join(string_list[::-1])
        
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        new_s = "%".join(s)
        new_s = new_s[::-1].split("%")
        for idx,(new,old) in  enumerate(zip(new_s,s)):
            s[idx] = new
        return s
        
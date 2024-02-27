class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_list =[str(integer) for integer in digits]
        final =[int(s) for s in  str(int(''.join(str_list)) + 1)]


        return final
        
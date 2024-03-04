class Solution:
    def smallestNumber(self, num: int) -> int:
        str_num = str(num)
        if str_num[0] == '-':
            nums_list = sorted(str_num[1:])
            return int('-' + ''.join(nums_list[::-1]))
        else:
            nums_list = sorted(str_num)
            if nums_list[0] == '0' and len(nums_list) > 1:
                non_zero_idx = next((i for i, n in enumerate(nums_list) if n != '0'), None)
                if non_zero_idx:
                    nums_list[0], nums_list[non_zero_idx] = nums_list[non_zero_idx], nums_list[0]
            return int(''.join(nums_list))

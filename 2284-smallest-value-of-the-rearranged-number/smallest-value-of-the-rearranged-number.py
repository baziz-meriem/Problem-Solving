class Solution:
    def smallestNumber(self, num: int) -> int:
        str_num= str(num)
        negative=False
        if str_num[0]=='-':
            negative=True
            str_num = str_num[1:]

        nums_list = sorted([int(num) for num in list(str_num)])

        if nums_list[0] == 0 and negative==False and len(nums_list)>1:
            idx=1
            while nums_list[idx]==0 and idx < len(nums_list)-1:
                idx += 1
            nums_list[idx],nums_list[0] =  nums_list[0],nums_list[idx]

        nums_list_str = [ str(num) for num in nums_list ] 

        if negative:
            out = int('-'+ ''.join(nums_list_str[::-1]))
        else:
            out = int(''.join(nums_list_str))

        return out
        

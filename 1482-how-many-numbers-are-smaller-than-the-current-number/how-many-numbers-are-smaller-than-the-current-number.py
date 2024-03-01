class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        my_dict={}
        for idx,num in enumerate(sorted(nums)):
            if num not in my_dict:
                my_dict[num]= idx
        print(my_dict)
        my_list=[]
        for val in nums:
            my_list.append(my_dict[val])
        return my_list

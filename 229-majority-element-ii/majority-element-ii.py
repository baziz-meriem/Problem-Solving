class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elements =[]
        min_occurence = len(nums)//3
        occurences_dict ={}
        for num in nums:
            if num in occurences_dict:
                occurences_dict[num] += 1
    
            else:
                occurences_dict[num] = 1

            if occurences_dict[num] > min_occurence and num not in elements:
                    elements.append(num)

        return elements


        
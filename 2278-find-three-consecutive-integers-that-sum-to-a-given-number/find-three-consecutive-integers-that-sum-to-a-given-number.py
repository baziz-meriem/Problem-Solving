class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num %3 != 0:
            #return an empty array
            return []
        else:
            #we substract 1 from the 1st integer and give it to the third (we will still have the same sum)
            return [int(num/3-1),int(num/3),int(num/3+1)]
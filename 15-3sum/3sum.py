from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        nums.sort()
        positives=[]
        negatives=[]
        triplets=set()

        for num in nums:
            if num>0:
                positives.append(num)
            else:
                negatives.append(num)

        if len(positives)==0  and counter[0]<3 or len(negatives)==0 and counter[0]<3 :
            return []

        if counter[0]>=3:
            triplets.add((0,0,0))

        for neg in negatives:
            for pos in positives:
                if  counter[-neg - pos]>1 or -neg - pos in counter.keys() and neg !=(-neg - pos) and pos !=(-neg - pos):
                   triplets.add(tuple(sorted((pos,neg,-neg - pos))))
        
        output =sorted([[*triplet] for triplet in triplets])
        return output



        
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        max = 1
        current = 1
        value = False

        for idx in range(len(arr)-1):

            if arr[idx] < arr[idx+1] and value == False :
                current += 1
            elif arr[idx] > arr[idx+1] and current > 1 :
                current +=1
                value = True
            elif  arr[idx] < arr[idx+1] and value == True:
                if current > max and value==True:
                    max = current
                current=2
                value = False

            else:
                current = 1

            if current > max and value==True:
                    max = current
        if max<=2:
            max = 0

        return max



        
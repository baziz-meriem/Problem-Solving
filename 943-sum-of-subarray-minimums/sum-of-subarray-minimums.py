class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        prevSmall=[-1]*n
        nextSmall=[n]* n
        stack = []
        sumSubarrays  = 0

        for idx,val in enumerate(arr):
            while stack and arr[stack[-1]]>=val:
                stack.pop()
            
            if stack:
                prevSmall[idx] = stack[-1]
            stack.append(idx)
        stack.clear()

        for idx in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>arr[idx]:
                stack.pop()
            
            if stack:
                nextSmall[idx] = stack[-1]
            stack.append(idx)

        modulo = 10**9 + 7 

        for i in range(n):
            left_count = i - prevSmall[i]
            right_count = nextSmall[i] - i
            sumSubarrays += left_count * right_count * arr[i]
            sumSubarrays %= modulo
        return sumSubarrays
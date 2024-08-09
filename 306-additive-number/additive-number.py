class Solution:
    def isAdditiveNumber(self,num):
        def backtrack(index, num1, num2):

            if index == len(num):
                return True
            
            next_num = str(int(num1) + int(num2))

            if not num.startswith(next_num, index):
                return False
            
            # Move the index to the end of the current valid number
            next_index = index + len(next_num)
            
            return backtrack(next_index, num2, next_num)
        
        n = len(num)

        for i in range(1, n):
            for j in range(i + 1, n):
                num1 = num[:i]
                num2 = num[i:j]
                
                # Skip invalid numbers with leading zeros
                if (num1.startswith('0') and len(num1) > 1) or (num2.startswith('0') and len(num2) > 1):
                    continue
                
                # Start the backtracking search with the current pair
                if backtrack(j, num1, num2):
                    return True
        
        return False

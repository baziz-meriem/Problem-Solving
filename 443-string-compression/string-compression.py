class Solution:
    def compress(self, chars: List[str]) -> int:
        current = 0
        idx = 0

        while idx <len(chars)-1:
            if chars[idx] == chars[idx+1]:
                index = idx + 1
                current += 1

                while index <= len(chars)-1 and chars[index] == chars[idx] :
                    print(index)
                    
                    index += 1
                    current += 1
                
                del chars[idx+1:index]

                if current>1:
                    chars[idx] += str(current)
                current = 0

                
            idx += 1
            
        chars[:] = [item for sublist in chars for item in sublist ]
            

        return len(chars)
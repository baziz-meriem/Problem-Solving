from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        write_idx = 0
        read_idx = 0

        while read_idx < len(chars):
            current_char = chars[read_idx]
            count = 0

            while read_idx < len(chars) and chars[read_idx] == current_char:
                read_idx += 1
                count += 1

            chars[write_idx] = current_char
            write_idx += 1

            if count > 1:
                for digit in str(count):
                    chars[write_idx] = digit
                    write_idx += 1

        return write_idx

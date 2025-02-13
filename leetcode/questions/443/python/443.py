from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = cur_idx = 0

        while i < len(chars):
            length = 0

            while i + length < len(chars) and chars[i] == chars[i + length]:
                length += 1

            chars[cur_idx] = chars[i]
            cur_idx += 1

            if length > 1:
                length_str = str(length)

                for digit in length_str:
                    chars[cur_idx] = digit
                    cur_idx += 1

            i += length

        return cur_idx
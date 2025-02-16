from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:       
        def build_sequence(idx = 0):
            if idx >= len_sequence:
                return True

            if sequence[idx] != 0:
                return build_sequence(idx + 1)

            for num in reversed(range(1, n + 1)):
                if is_used[num]:
                    continue

                is_used[num] = True
                sequence[idx] = num

                if num == 1:
                    if build_sequence(idx + 1):
                        return True

                elif 0 <= (idx + num) < len(sequence) and sequence[idx + num] == 0:
                    sequence[idx + num] = num

                    if build_sequence(idx + 1):
                        return True

                    sequence[idx + num] = 0

                sequence[idx] = 0
                is_used[num] = False

            return False

        len_sequence = (n * 2 - 1)
        sequence = [0] * len_sequence
        is_used = [False] * (n + 1)
        build_sequence()

        return sequence
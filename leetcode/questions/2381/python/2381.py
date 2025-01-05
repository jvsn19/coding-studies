from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        def ctoi(c):
            return ord(c) - ord('a')

        def itoc(i):
            return chr(i % 26 + ord('a'))

        shift_cnt = [0] * (len(s) + 1)

        for st, end, direction in shifts:
            shift_cnt[st] += (-1 if direction == 0 else 1)
            shift_cnt[end + 1] += (1 if direction == 0 else -1)

        ans = [ord(c) - ord('a') for c in s]
        cur_shift = 0

        for idx in range(len(ans)):
            cur_shift += shift_cnt[idx]
            ans[idx] = itoc(ans[idx] + cur_shift)

        return ''.join(ans)
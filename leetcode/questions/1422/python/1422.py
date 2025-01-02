class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = s.count('1')
        total_zeroes = 0
        max_score = 0

        # len(s) -1 to avoid all the string being at the left substring
        for idx in range(len(s) - 1):
            c = s[idx]

            if c == '0':
                total_zeroes += 1
            else:
                total_ones -= 1

            max_score = max(max_score, total_zeroes + total_ones)

        return max_score
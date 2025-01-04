class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        def ctoi(c):
            return ord(c) - ord('a')

        first, last = {}, {}

        # Save the first and last occurences of each char in 's'
        for idx, c in enumerate(s):
            if c not in first:
                first[c] = idx
            last[c] = idx

        ans = 0

        # For each char saved get the start and end range, run over 's' and count how many different
        # letters exists between (start, end) (bitmask is a good option)
        for c in first:
            st, end = first[c], last[c]
            mask = 0

            for idx in range(st + 1, end):
                # If this bit is not set yet, the char wasn't found before. ans += 1
                if mask & (1 << ctoi(s[idx])) == 0:
                    ans += 1
                mask |= (1 << ctoi(s[idx]))

        return ans
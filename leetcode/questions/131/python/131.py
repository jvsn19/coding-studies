from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def get_palindromes(st, partition):
            if st >= len_s:
                palindromes.append(partition)
                return

            for end in range(st, len(s)):
                # end - st < 3 => strings with length 1 or 2 which is_palindrome[st + 1][end - 1] doesn't work
                if s[st] == s[end] and ((end - st < 3) or is_palindrome[st + 1][end - 1]):
                    is_palindrome[st][end] = True
                    get_palindromes(end + 1, partition + [s[st:end + 1]])

        palindromes = []
        len_s = len(s)
        is_palindrome = [[False for _ in range(len_s)] for _ in range(len_s)]
        get_palindromes(0, [])

        return palindromes
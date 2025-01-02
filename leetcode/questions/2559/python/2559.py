from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix_sum = [0] * (len(words) + 1)
        vowels = 'aeiou'

        for idx, word in enumerate(words):
            prefix_sum[idx + 1] = prefix_sum[idx] + (word[0] in vowels and word[~0] in vowels)

        ans = []

        for l, r in queries: 
            ans.append(prefix_sum[r + 1] - prefix_sum[l])

        return ans
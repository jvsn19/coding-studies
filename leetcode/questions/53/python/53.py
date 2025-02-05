from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        INF = float('inf')
        max_sum = cur_sum = -INF

        for num in nums:
            cur_sum = num if cur_sum < 0 else num + cur_sum
            max_sum = max(max_sum, cur_sum)

        return max_sum
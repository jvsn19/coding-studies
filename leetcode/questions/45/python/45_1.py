from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        len_nums = len(nums)

        def jump_impl(idx = 0, prev = 0):
            if idx >= len_nums - 1:
                return 0

            if idx in memo:
                return memo[idx]

            jumps = float('inf')

            for next_idx in range(idx + 1, min(len_nums, idx + nums[idx]) + 1):
                jumps = min(jumps, jump_impl(next_idx, idx) + 1)

            memo[idx] = jumps

            return memo[idx]

        return jump_impl()
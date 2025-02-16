from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        longest_jump = 0
        reachable = 0
        jumps = 0

        for idx, num in enumerate(nums):
            longest_jump = max(longest_jump, idx + num)

            if reachable >= len(nums) - 1:
                return jumps

            if idx == reachable:
                jumps += 1
                reachable = longest_jump

        return jumps
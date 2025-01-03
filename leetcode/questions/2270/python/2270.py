from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums)
        num_splits = 0

        for idx in range(len(nums) - 1):
            num = nums[idx]
            left_sum += num
            right_sum -= num

            if left_sum >= right_sum:
                num_splits += 1

        return num_splits
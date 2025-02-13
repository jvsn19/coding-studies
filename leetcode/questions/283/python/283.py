from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero = 0

        for idx in range(len(nums)):
            nums[idx], nums[non_zero] = nums[non_zero], nums[idx]
            
            if nums[non_zero] != 0:
                non_zero += 1        
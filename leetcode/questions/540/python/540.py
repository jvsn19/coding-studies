from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) >> 1) 

            if m > 0 and nums[m] == nums[m - 1]:
                m -= 1

            if m < len(nums) - 1 and nums[m] != nums[m + 1] or m == len(nums) - 1:
                return nums[m]

            if m & 1:
                r = m
            else:
                l = m + 1
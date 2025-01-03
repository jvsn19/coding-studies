from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, leftmost = True):
            l, r = 0, len(nums)

            while l < r:
                m = l + ((r - l) >> 1)

                if (leftmost and nums[m] < target) or (not leftmost and nums[m] <= target):
                    l = m + 1
                else: 
                    r = m

            if leftmost:
                return l if (0 <= l < len(nums) and nums[l] == target) else -1
            
            r -= 1

            return r if (0 <= r < len(nums) and nums[r] == target) else -1

        return [binary_search(nums, target), binary_search(nums, target, False)]
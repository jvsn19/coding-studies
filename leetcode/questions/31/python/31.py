from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def revert(st, end):
            while st < end:
                nums[st], nums[end] = nums[end], nums[st]
                st += 1
                end -= 1

        last = len(nums) - 1

        # from the end find the first decreasing pair
        first_small = last - 1

        while first_small > -1 and nums[first_small] >= nums[first_small + 1]:
            first_small -= 1

        if first_small != -1:
            # swap the biggest value with the smallest value on the right part
            first_big = last

            while nums[first_big] <= nums[first_small]:
                first_big -= 1
            
            nums[first_small], nums[first_big] = nums[first_big], nums[first_small]
            
        revert(first_small + 1, last)
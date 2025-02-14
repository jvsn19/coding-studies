from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def revert(st, end):
            while st < end:
                nums[st], nums[end] = nums[end], nums[st]
                st += 1
                end -= 1
        
        len_nums = len(nums)
        k %= len_nums
        revert(0, len_nums - 1)
        revert(0, k - 1)
        revert(k, len_nums - 1)
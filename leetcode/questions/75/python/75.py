class Solution:
    def sortColors(self, nums):
        len_nums = len(nums)
        idx, color_a, color_b = 0, 0, len_nums - 1

        while idx <= color_b:
            if nums[idx] == 0:
                nums[idx], nums[color_a] = nums[color_a], nums[idx]
                color_a += 1
                idx += 1

            elif nums[idx] == 2:
                nums[idx], nums[color_b] = nums[color_b], nums[idx]
                color_b -= 1

            else:
                idx += 1
class Solution(object):
    def removeDuplicates(self, nums):
        last = 1

        for idx in range(1, len(nums)):
            if nums[idx] != nums[idx - 1]:
                nums[last] = nums[idx]
                last += 1

        return last
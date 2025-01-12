class Solution(object):
    def removeElement(self, nums, val):
        last = len(nums) - 1

        for idx in reversed(range(len(nums))):
            if nums[idx] == val:
                nums[idx], nums[last] = nums[last], nums[idx]
                last -= 1
        
        return last + 1
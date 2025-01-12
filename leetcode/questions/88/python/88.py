from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums2_limit = len(nums2)
        nums1_limit = len(nums1) - nums2_limit
        idx1 = nums1_limit - 1
        idx2 = nums2_limit - 1

        for idx_merged in reversed(range(len(nums1))):
            if idx2 >= 0 and (idx1 < 0 or nums1[idx1] <= nums2[idx2]):
                nums1[idx_merged] = nums2[idx2]
                idx2 -= 1
            elif idx2 < 0 or nums1[idx1] > nums2[idx2]:
                nums1[idx_merged] = nums1[idx1]
                idx1 -= 1
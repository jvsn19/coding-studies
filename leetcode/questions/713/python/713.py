class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        prod = 1
        left = 0

        for right, num in enumerate(nums):
            prod *= num

            while left <= right and prod >= k:
                prod //= nums[left]
                left += 1

            ans += (right - left + 1)

        return ans
from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def get_digit_sum(num):
            return sum([ord(digit) - ord('0') for digit in str(num)])

        INF = float('inf')
        prev_sum = {}
        ans = -INF

        for idx, num in enumerate(nums):
            digit_sum = get_digit_sum(num)
            prev_idx = prev_sum.get(digit_sum)

            if prev_idx is not None:
                ans = max(ans, num + nums[prev_idx])
            
            if prev_idx is None or nums[prev_idx] < num:
                prev_sum[digit_sum] = idx

        return ans if ans != -INF else -1
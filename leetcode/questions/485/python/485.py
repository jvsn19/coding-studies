from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cnt = cur_cnt = 0

        for num in nums:
            cur_cnt = (cur_cnt * num) + num
            max_cnt = max(max_cnt, cur_cnt)

        return max_cnt
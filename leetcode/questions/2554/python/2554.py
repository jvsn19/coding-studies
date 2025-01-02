from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = {num for num in banned if num <= n}
        cur_sum = 0
        cur_cnt = 0

        for num in range(1, n + 1):
            if num + cur_sum > maxSum:
                break
            if num not in banned:
                cur_sum += num
                cur_cnt += 1
        
        return cur_cnt
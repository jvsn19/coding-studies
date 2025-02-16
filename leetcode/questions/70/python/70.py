class Solution:
    def climbStairs(self, n: int) -> int:
        prev_one, prev_two = 1, 0

        for _ in range(n):
            prev_one, prev_two = prev_one + prev_two, prev_one

        return prev_one
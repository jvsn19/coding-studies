class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        invert = n < 0
        n = abs(n)

        while n:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1

        return 1/ans if invert else ans
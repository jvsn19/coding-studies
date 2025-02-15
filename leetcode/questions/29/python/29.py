class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_VAL, MAX_VAL = -2**31, 2**31 - 1
        is_neg = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        base = divisor
        quocient = 1
        ans = 0

        while dividend >= divisor:
            while dividend > (divisor << 1):
                quocient <<= 1
                divisor <<= 1

            ans += quocient
            dividend -= divisor
            divisor = base
            quocient = 1

        if is_neg:
            ans *= -1

        if MIN_VAL <= ans <= MAX_VAL:
            return ans

        return MAX_VAL if ans > MAX_VAL else MIN_VAL
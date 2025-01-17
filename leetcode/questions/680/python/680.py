class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(left, right, previously_deleted):
            while left < right:
                if previously_deleted:
                    return False
                
                if s[left] != s[right]:
                    return check(left + 1, right, True) or check(left, right - 1, True)

                left += 1
                right -= 1

            return True

        return check(0, len(s) - 1, False)
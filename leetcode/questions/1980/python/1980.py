from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        values = {int(num, 2) for num in nums}
        missing = 0
        binary = []

        while missing in values:
            missing += 1

        while len(binary) < len(nums):
            binary.append('1' if missing & 1 else '0')
            missing >>= 1

        return ''.join(binary[::-1])